

platforms = ["GalagoPro3",
  "KabylakeRvp3",
  "UpXtreme",
  "WhiskeylakeURvp",
  "CometlakeURvp"]

target = ["RELEASE", "DEBUG"]
toolset = "GCC5"

intel_link = lambda path, platform, target : f"[{platform}_{target}_{toolset}](https://nightly.link/naitaku/edk2-platforms-build/workflows/build-{path}-platforms/main/{platform}_{target}_{toolset}.zip)"

def makelinks (platforms, path):
    print("| Platform | RELEASE | DEBUG |\n| -------- | ------- | ----- |")
    for platform in platforms:
        print(f"| {platform} | {intel_link(path, platform, 'RELEASE')} | {intel_link(path, platform, 'DEBUG')} |")

print("### Intel")
platforms = ["GalagoPro3",
  "KabylakeRvp3",
  "UpXtreme",
  "WhiskeylakeURvp",
  "CometlakeURvp"]
makelinks(platforms, "intel")

print("### Raspberry Pi")
platforms = ["RPi3_AARCH64","RPi4_AARCH64"]
makelinks(platforms, "edk2")

print("### Arm")
platforms = ["ArmJuno_AARCH64","Sgi575_AARCH64"]
makelinks(platforms, "edk2")

print("### BeagleBoard")
platforms = ["BeagleBoard_ARM"]
makelinks(platforms, "edk2")

print("### SiFive (RISC-V)")
platforms = ["FreedomU500VC707_RISCV64", "FreedomU540HiFiveUnleashed_RISCV64"]
makelinks(platforms, "edk2")

print("### Socionext")
platforms = ["DeveloperBox_AARCH64"]
makelinks(platforms, "edk2")




