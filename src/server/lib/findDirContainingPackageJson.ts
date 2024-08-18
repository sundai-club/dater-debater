import { promises as fs } from "fs";
import { join, dirname } from "path";

export async function findDirContainingPackageJson(
  startDir: string,
): Promise<string> {
  let currentDir = startDir;

  while (true) {
    try {
      await fs.access(join(currentDir, "package-lock.json"));
      return currentDir;
    } catch {
      const parentDir = dirname(currentDir);
      if (parentDir === currentDir) {
        throw new Error("Could not find package.json in any parent directory");
      }
      currentDir = parentDir;
    }
  }
}
