import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Build output directory moved to avoid OneDrive/file-lock conflicts on .next
  distDir: ".next-build-run",
};

export default nextConfig;
