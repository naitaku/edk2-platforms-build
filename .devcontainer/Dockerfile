FROM ghcr.io/sarisia/vscode-dev-containers-multiarch/base:ubuntu-20.04

ARG USERNAME=vscode

# Use bash
SHELL ["/bin/bash", "-c"]

# install development tools
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    # common for EDK2
    git \
    python3-distutils \
    build-essential \
    nasm \
    acpica-tools \
    uuid-dev \
    # clang
    clang \
    llvm-dev \
    lld \
    # for cross-compile
    crossbuild-essential-i386 \
    crossbuild-essential-amd64 \
    crossbuild-essential-arm64 \
    crossbuild-essential-armel \
    gcc-riscv64-unknown-elf \
    binutils-multiarch \
    # ARM
    device-tree-compiler \
    # Capsule
    gcab \
 && apt-get clean -y

# switch to unprivileged
USER ${USERNAME}
WORKDIR /home/${USERNAME}

# build EDK II
RUN git clone https://github.com/naitaku/edk2-platforms-build.git \
    && cd edk2-platforms-build \
    && git submodule update --init \
    && git submodule foreach git submodule update --init --force --depth=1

ENV GCC5_ARM_PREFIX=arm-linux-gnueabi-
ENV GCC5_AARCH64_PREFIX=aarch64-linux-gnu-
ENV GCC5_RISCV64_PREFIX=riscv64-unknown-elf-
ENV GCC5_BIN=x86_64-linux-gnu-
ENV CLANG38_BIN=/usr/lib/llvm-10/bin/
ENV WORKSPACE=/home/${USERNAME}/edk2-platforms-build
ENV PACKAGES_PATH=${WORKSPACE}/edk2:${WORKSPACE}/edk2-platforms:${WORKSPACE}/edk2-non-osi
WORKDIR ${WORKSPACE}

RUN . edk2/edksetup.sh \
    && make -C edk2/BaseTools
