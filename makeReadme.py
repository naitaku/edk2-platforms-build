header = '''
# Unofficial edk2-platforms nightly build 

This repository provides unofficial
[tianocore/edk2-platforms](https://github.com/tianocore/edk2-platforms)
nightly build.

Built binaries are saved as artifacts in Github Actions.
You can download them from here. Github login is required to download the artifacts.

https://github.com/naitaku/edk2-platforms-build/actions?query=branch%3Amain+event%3Apush

They will be retained for 90 days.

## The latest built binaries

The links below don't require your Github login.
'''

target = ["RELEASE", "DEBUG"]
toolset = "GCC5"

intel_link = lambda path, platform, target : f"[{platform}_{target}_{toolset}](https://nightly.link/naitaku/edk2-platforms-build/workflows/build-{path}-platforms/main/{platform}_{target}_{toolset}.zip)"

def makelinks (platforms, path):
    print("| Platform | RELEASE | DEBUG |\n| -------- | ------- | ----- |")
    for platform in platforms:
        print(f"| {platform} | {intel_link(path, platform, 'RELEASE')} | {intel_link(path, platform, 'DEBUG')} |")

def title(str):
  print(f"\n{str}\n")

print(header)
title("### Intel")
platforms = ["GalagoPro3",
  "KabylakeRvp3",
  "UpXtreme",
  "WhiskeylakeURvp",
  "CometlakeURvp"]
makelinks(platforms, "intel")

title("### Raspberry Pi")
platforms = ["RPi3_AARCH64","RPi4_AARCH64"]
makelinks(platforms, "edk2")

title("### Arm")
platforms = ["ArmJuno_AARCH64","Sgi575_AARCH64"]
makelinks(platforms, "edk2")

title("### BeagleBoard")
platforms = ["BeagleBoard_ARM"]
makelinks(platforms, "edk2")

title("### SiFive (RISC-V)")
platforms = ["FreedomU500VC707_RISCV64", "FreedomU540HiFiveUnleashed_RISCV64"]
makelinks(platforms, "edk2")

title("### Socionext")
platforms = ["DeveloperBox_AARCH64"]
makelinks(platforms, "edk2")




