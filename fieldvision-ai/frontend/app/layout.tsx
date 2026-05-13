import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "FieldVision AI | IPL T20 2026",
  description: "AI match command center for IPL T20 2026 decisions.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
