import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { Providers } from "./providers";
import { Sidebar } from "@/components/Sidebar";
import { MobileHeader } from "@/components/MobileHeader";
import { getChapterStats } from "@/lib/data";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "CBSE Class 12 Maths PYQ | Previous Year Questions",
  description:
    "Practice CBSE Class 12 Mathematics Previous Year Questions chapter-wise with detailed solutions. 2015–2025 papers.",
  openGraph: {
    title: "CBSE Class 12 Maths PYQ",
    description: "Chapter-wise Previous Year Questions with solutions. 2015–2025.",
    images: [{ url: "/logo.svg", width: 540, height: 540 }],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const stats = getChapterStats();

  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        <Providers>
          <div className="flex h-screen bg-slate-50 overflow-hidden">
            {/* Desktop Sidebar */}
            <div className="hidden lg:flex">
              <Sidebar stats={stats} />
            </div>

            {/* Main content */}
            <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
              {/* Desktop top bar */}
              <header className="hidden lg:flex items-center justify-between px-6 py-3 border-b border-slate-200 bg-white/80 backdrop-blur sticky top-0 z-30">
                <div className="text-sm text-slate-500">
                  CBSE Class 12 Mathematics — Previous Year Questions
                </div>
                <span className="text-xs font-medium text-white bg-blue-600 rounded-full px-3 py-1">
                  Built by Abilash
                </span>
              </header>

              {/* Mobile header */}
              <MobileHeader stats={stats} />

              {/* Page content */}
              <main className="flex-1 overflow-y-auto">
                {children}
              </main>
            </div>
          </div>
        </Providers>
      </body>
    </html>
  );
}
