// Turns a declarative graph spec (```plot blocks in solutions) into SVG primitives.
// Shared by the content checker (validation) and the <Plot> component (rendering).

export type PlotSpec = {
  x: [number, number];
  y: [number, number];
  lines?: { a: number; b: number; c: number; label?: string; dash?: boolean }[];
  fns?: { f: string; from?: number; to?: number; label?: string; dash?: boolean }[];
  params?: { x: string; y: string; t: [number, number]; label?: string; dash?: boolean }[];
  circles?: { cx: number; cy: number; r: number; label?: string; dash?: boolean }[];
  ellipses?: { cx: number; cy: number; rx: number; ry: number; label?: string; dash?: boolean }[];
  polygons?: { pts: [number, number][]; label?: string }[];
  areas?: { upper: string; lower?: string; from: number; to: number; label?: string }[];
  points?: { x: number; y: number; label?: string }[];
  labels?: { x: number; y: number; text: string }[];
};

export type Prim =
  | { kind: "grid"; d: string }
  | { kind: "axis"; d: string }
  | { kind: "tick"; x: number; y: number; text: string; anchor: "middle" | "end" }
  | { kind: "region"; d: string }
  | { kind: "curve"; d: string; dash: boolean; series: number }
  | { kind: "point"; x: number; y: number }
  | { kind: "label"; x: number; y: number; text: string; anchor: "start" | "middle" | "end"; series?: number };

export type CompiledPlot = { width: number; height: number; prims: Prim[] };

const KEYS = new Set(["x", "y", "lines", "fns", "params", "circles", "ellipses", "polygons", "areas", "points", "labels"]);

export function makeFn(expr: string, v = "x"): (n: number) => number {
  if (!/^[\w\s+\-*/().,%<>=?:!&|]*$/.test(expr)) throw new Error(`illegal characters in expression "${expr}"`);
  const body = `const {abs,sqrt,cbrt,sin,cos,tan,asin,acos,atan,exp,log,log10,pow,min,max,PI,E,sign,floor,ceil}=Math;return (${expr});`;
  return new Function(v, body) as (n: number) => number;
}

function niceStep(span: number) {
  const raw = span / 10;
  const p = Math.pow(10, Math.floor(Math.log10(raw)));
  for (const m of [1, 2, 5, 10]) if (raw <= m * p) return m * p;
  return 10 * p;
}

const fmt = (n: number) => (Math.abs(n) < 1e-9 ? "0" : String(+n.toFixed(2)));

export function compilePlot(spec: PlotSpec): CompiledPlot {
  for (const k of Object.keys(spec)) if (!KEYS.has(k)) throw new Error(`unknown plot key "${k}"`);
  const [x0, x1] = spec.x;
  const [y0, y1] = spec.y;
  if (!(x1 > x0 && y1 > y0)) throw new Error("plot ranges must be increasing");
  const W = 520;
  const pad = 28;
  const sx0 = (W - 2 * pad) / (x1 - x0);
  let sy = sx0;
  let H = (y1 - y0) * sy + 2 * pad;
  if (H > 560 || H < 220) {
    H = Math.min(560, Math.max(260, H));
    sy = (H - 2 * pad) / (y1 - y0);
  }
  const sx = sx0;
  const X = (x: number) => pad + (x - x0) * sx;
  const Y = (y: number) => H - pad - (y - y0) * sy;
  const r2 = (n: number) => Math.round(n * 10) / 10;
  const prims: Prim[] = [];

  // grid + ticks
  const stx = niceStep(x1 - x0);
  const sty = niceStep(y1 - y0);
  let g = "";
  for (let v = Math.ceil(x0 / stx) * stx; v <= x1 + 1e-9; v += stx) g += `M${r2(X(v))} ${r2(Y(y0))}V${r2(Y(y1))}`;
  for (let v = Math.ceil(y0 / sty) * sty; v <= y1 + 1e-9; v += sty) g += `M${r2(X(x0))} ${r2(Y(v))}H${r2(X(x1))}`;
  prims.push({ kind: "grid", d: g });
  const ax = Math.min(Math.max(0, x0), x1);
  const ay = Math.min(Math.max(0, y0), y1);

  // shaded regions first (under curves)
  for (const p of spec.polygons ?? []) {
    prims.push({ kind: "region", d: "M" + p.pts.map(([a, b]) => `${r2(X(a))} ${r2(Y(b))}`).join("L") + "Z" });
  }
  for (const a of spec.areas ?? []) {
    const fu = makeFn(a.upper);
    const fl = makeFn(a.lower ?? "0");
    const N = 160;
    const up: string[] = [];
    const lo: string[] = [];
    for (let i = 0; i <= N; i++) {
      const x = a.from + ((a.to - a.from) * i) / N;
      const u = fu(x), l = fl(x);
      if (!Number.isFinite(u) || !Number.isFinite(l)) throw new Error(`area expression not finite at x=${x}`);
      up.push(`${r2(X(x))} ${r2(Y(u))}`);
      lo.unshift(`${r2(X(x))} ${r2(Y(l))}`);
    }
    prims.push({ kind: "region", d: "M" + up.join("L") + "L" + lo.join("L") + "Z" });
  }

  // axes
  prims.push({ kind: "axis", d: `M${r2(X(x0))} ${r2(Y(ay))}H${r2(X(x1))}M${r2(X(ax))} ${r2(Y(y0))}V${r2(Y(y1))}` });
  for (let v = Math.ceil(x0 / stx) * stx; v <= x1 + 1e-9; v += stx)
    if (Math.abs(v) > 1e-9) prims.push({ kind: "tick", x: r2(X(v)), y: r2(Y(ay) + 14), text: fmt(v), anchor: "middle" });
  for (let v = Math.ceil(y0 / sty) * sty; v <= y1 + 1e-9; v += sty)
    if (Math.abs(v) > 1e-9) prims.push({ kind: "tick", x: r2(X(ax) - 5), y: r2(Y(v) + 4), text: fmt(v), anchor: "end" });
  prims.push({ kind: "tick", x: r2(X(ax) - 5), y: r2(Y(ay) + 14), text: "O", anchor: "end" });

  let series = 0;
  const labelAt = (x: number, y: number, text: string | undefined, s: number) => {
    if (!text) return;
    const inside = x >= x0 && x <= x1 && y >= y0 && y <= y1;
    if (!inside) return;
    const anchor = X(x) > W * 0.7 ? "end" : "start";
    prims.push({ kind: "label", x: r2(X(x) + (anchor === "end" ? -6 : 6)), y: r2(Y(y) - 6), text, anchor, series: s });
  };

  // straight lines ax + by = c clipped to the window
  for (const l of spec.lines ?? []) {
    const pts: [number, number][] = [];
    if (Math.abs(l.b) > 1e-12) {
      for (const x of [x0, x1]) pts.push([x, (l.c - l.a * x) / l.b]);
    }
    if (Math.abs(l.a) > 1e-12) {
      for (const y of [y0, y1]) pts.push([(l.c - l.b * y) / l.a, y]);
    }
    const inBox = pts.filter(([x, y]) => x >= x0 - 1e-9 && x <= x1 + 1e-9 && y >= y0 - 1e-9 && y <= y1 + 1e-9);
    inBox.sort((p, q) => p[0] - q[0] || p[1] - q[1]);
    if (inBox.length < 2) throw new Error(`line ${l.a}x + ${l.b}y = ${l.c} does not cross the window`);
    const [p, q] = [inBox[0], inBox[inBox.length - 1]];
    prims.push({ kind: "curve", d: `M${r2(X(p[0]))} ${r2(Y(p[1]))}L${r2(X(q[0]))} ${r2(Y(q[1]))}`, dash: !!l.dash, series });
    const t = 0.82;
    labelAt(p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t, l.label, series);
    series++;
  }

  const sample = (fx: (t: number) => number, fy: (t: number) => number, t0: number, t1: number, n: number) => {
    let d = "";
    let pen = false;
    let last: [number, number] | null = null;
    const ylo = y0 - (y1 - y0), yhi = y1 + (y1 - y0);
    for (let i = 0; i <= n; i++) {
      const t = t0 + ((t1 - t0) * i) / n;
      const x = fx(t), y = fy(t);
      if (!Number.isFinite(x) || !Number.isFinite(y) || y < ylo || y > yhi) { pen = false; continue; }
      d += `${pen ? "L" : "M"}${r2(X(x))} ${r2(Y(y))}`;
      pen = true;
      if (x >= x0 && x <= x1 && y >= y0 && y <= y1) last = [x, y];
    }
    if (!d) throw new Error("curve has no finite points in the window");
    return { d, last };
  };

  for (const f of spec.fns ?? []) {
    const fn = makeFn(f.f);
    const { d, last } = sample((t) => t, fn, f.from ?? x0, f.to ?? x1, 240);
    prims.push({ kind: "curve", d, dash: !!f.dash, series });
    if (last) labelAt(last[0], last[1], f.label, series);
    series++;
  }
  for (const p of spec.params ?? []) {
    const fx = makeFn(p.x, "t"), fy = makeFn(p.y, "t");
    const { d, last } = sample(fx, fy, p.t[0], p.t[1], 240);
    prims.push({ kind: "curve", d, dash: !!p.dash, series });
    if (last) labelAt(last[0], last[1], p.label, series);
    series++;
  }
  for (const c of [...(spec.circles ?? []).map((c) => ({ ...c, rx: c.r, ry: c.r })), ...(spec.ellipses ?? [])]) {
    const { d } = sample((t) => c.cx + c.rx * Math.cos(t), (t) => c.cy + c.ry * Math.sin(t), 0, 2 * Math.PI, 180);
    prims.push({ kind: "curve", d: d + "Z", dash: !!c.dash, series });
    labelAt(c.cx + c.rx * Math.cos(Math.PI / 4), c.cy + c.ry * Math.sin(Math.PI / 4), c.label, series);
    series++;
  }
  for (const p of spec.points ?? []) {
    prims.push({ kind: "point", x: r2(X(p.x)), y: r2(Y(p.y)) });
    if (p.label) {
      const anchor = X(p.x) > W * 0.75 ? "end" : "start";
      prims.push({ kind: "label", x: r2(X(p.x) + (anchor === "end" ? -7 : 7)), y: r2(Y(p.y) - 7), text: p.label, anchor });
    }
  }
  for (const l of spec.labels ?? []) prims.push({ kind: "label", x: r2(X(l.x)), y: r2(Y(l.y)), text: l.text, anchor: "middle" });
  return { width: W, height: Math.round(H), prims };
}
