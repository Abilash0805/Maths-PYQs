export function LogoMark({ className = "size-9" }: { className?: string }) {
  return (
    <svg viewBox="0 0 40 40" className={className} aria-hidden="true">
      <rect width="40" height="40" rx="11" fill="var(--primary)" />
      <path
        d="M24.8 8.6c-2.6-.6-4.4.9-5 4l-2.6 14.2c-.4 2.2-1.6 3.2-3.4 2.7"
        fill="none"
        stroke="var(--primary-ink)"
        strokeWidth="2.6"
        strokeLinecap="round"
      />
      <circle cx="29.2" cy="27.6" r="2.6" fill="var(--accent)" />
    </svg>
  );
}
