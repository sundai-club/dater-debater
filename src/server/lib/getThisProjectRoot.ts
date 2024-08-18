import { findDirContainingPackageJson } from "@/server/lib/findDirContainingPackageJson";
import { resolve } from "path";

export async function getThisProjectRoot(): Promise<string> {
  const startDir = resolve(__dirname);
  return findDirContainingPackageJson(startDir);
}
