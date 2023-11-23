#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v2
# autospec commit: 250a666
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xorg-server
Version  : 21.1.9
Release  : 390
URL      : https://www.x.org/releases/individual/xserver/xorg-server-21.1.9.tar.gz
Source0  : https://www.x.org/releases/individual/xserver/xorg-server-21.1.9.tar.gz
Source1  : https://www.x.org/releases/individual/xserver/xorg-server-21.1.9.tar.gz.sig
Summary  : Modular X.Org X Server
Group    : Development/Tools
License  : MIT
Requires: xorg-server-bin = %{version}-%{release}
Requires: xorg-server-data = %{version}-%{release}
Requires: xorg-server-lib = %{version}-%{release}
Requires: xorg-server-license = %{version}-%{release}
Requires: xorg-server-man = %{version}-%{release}
Requires: xorg-server-setuid = %{version}-%{release}
Requires: xf86-input-libinput
Requires: xf86-video-amdgpu
Requires: xf86-video-ati
Requires: xf86-video-fbdev
Requires: xf86-video-nouveau
Requires: xf86-video-vesa
Requires: xwayland
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : font-util-dev
BuildRequires : freetype-dev
BuildRequires : graphviz
BuildRequires : libdmx-dev
BuildRequires : libgcrypt-dev
BuildRequires : libxshmfence-dev
BuildRequires : libxslt-bin
BuildRequires : nettle-dev
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libbsd-overlay)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(libxcvt)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xf86dgaproto)
BuildRequires : pkgconfig(xfont)
BuildRequires : pkgconfig(xfont2)
BuildRequires : pkgconfig(xkbcomp)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : xkbcomp-bin
BuildRequires : xmlto
BuildRequires : xtrans-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-add-default-keyboard-setup-for-xorg.patch

%description
This is a submodule to access linux framebuffer devices.
It is supported to work as helper module (like vgahw)
for the chipset drivers.  There are functions for
saving/restoring/setting video modes, set palette entries,
and a few more helper functions.  Some of them can be
hooked directly into ScrnInfoRec.

%package bin
Summary: bin components for the xorg-server package.
Group: Binaries
Requires: xorg-server-data = %{version}-%{release}
Requires: xorg-server-setuid = %{version}-%{release}
Requires: xorg-server-license = %{version}-%{release}

%description bin
bin components for the xorg-server package.


%package data
Summary: data components for the xorg-server package.
Group: Data

%description data
data components for the xorg-server package.


%package dev
Summary: dev components for the xorg-server package.
Group: Development
Requires: xorg-server-lib = %{version}-%{release}
Requires: xorg-server-bin = %{version}-%{release}
Requires: xorg-server-data = %{version}-%{release}
Provides: xorg-server-devel = %{version}-%{release}
Requires: xorg-server = %{version}-%{release}

%description dev
dev components for the xorg-server package.


%package lib
Summary: lib components for the xorg-server package.
Group: Libraries
Requires: xorg-server-data = %{version}-%{release}
Requires: xorg-server-license = %{version}-%{release}

%description lib
lib components for the xorg-server package.


%package license
Summary: license components for the xorg-server package.
Group: Default

%description license
license components for the xorg-server package.


%package man
Summary: man components for the xorg-server package.
Group: Default

%description man
man components for the xorg-server package.


%package setuid
Summary: setuid components for the xorg-server package.
Group: Default

%description setuid
setuid components for the xorg-server package.


%prep
%setup -q -n xorg-server-21.1.9
cd %{_builddir}/xorg-server-21.1.9
%patch -P 1 -p1
pushd ..
cp -a xorg-server-21.1.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698252035
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
mkdir -p %{buildroot}/usr/share/package-licenses/xorg-server
cp %{_builddir}/xorg-server-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xorg-server/11d1ae389a1a78f7832586e4c2a0c3c7263b7475 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/Xwayland
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/X11/xorg.conf.d/
cp 00-keyboard.conf %{buildroot}/usr/share/defaults/etc/X11/xorg.conf.d/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name} --skip-path /usr/bin/Xorg

%files
%defattr(-,root,root,-)
/usr/lib64/xorg/protocol.txt

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/Xnest
/V3/usr/bin/Xvfb
/V3/usr/bin/gtf
/usr/bin/X
/usr/bin/Xnest
/usr/bin/Xvfb
/usr/bin/gtf

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/10-quirks.conf
/usr/share/defaults/etc/X11/xorg.conf.d/00-keyboard.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/XIstubs.h
/usr/include/xorg/Xprintf.h
/usr/include/xorg/callback.h
/usr/include/xorg/client.h
/usr/include/xorg/closestr.h
/usr/include/xorg/closure.h
/usr/include/xorg/colormap.h
/usr/include/xorg/colormapst.h
/usr/include/xorg/compiler.h
/usr/include/xorg/compositeext.h
/usr/include/xorg/cursor.h
/usr/include/xorg/cursorstr.h
/usr/include/xorg/damage.h
/usr/include/xorg/damagestr.h
/usr/include/xorg/dbestruct.h
/usr/include/xorg/dgaproc.h
/usr/include/xorg/displaymode.h
/usr/include/xorg/dix.h
/usr/include/xorg/dixaccess.h
/usr/include/xorg/dixevents.h
/usr/include/xorg/dixfont.h
/usr/include/xorg/dixfontstr.h
/usr/include/xorg/dixgrabs.h
/usr/include/xorg/dixstruct.h
/usr/include/xorg/dri.h
/usr/include/xorg/dri2.h
/usr/include/xorg/dri3.h
/usr/include/xorg/dristruct.h
/usr/include/xorg/edid.h
/usr/include/xorg/events.h
/usr/include/xorg/exa.h
/usr/include/xorg/exevents.h
/usr/include/xorg/extension.h
/usr/include/xorg/extinit.h
/usr/include/xorg/extnsionst.h
/usr/include/xorg/fb.h
/usr/include/xorg/fbdevhw.h
/usr/include/xorg/fboverlay.h
/usr/include/xorg/fbpict.h
/usr/include/xorg/fbrop.h
/usr/include/xorg/fourcc.h
/usr/include/xorg/gc.h
/usr/include/xorg/gcstruct.h
/usr/include/xorg/geext.h
/usr/include/xorg/geint.h
/usr/include/xorg/glamor.h
/usr/include/xorg/globals.h
/usr/include/xorg/glx_extinit.h
/usr/include/xorg/glxvndabi.h
/usr/include/xorg/glyphstr.h
/usr/include/xorg/hotplug.h
/usr/include/xorg/i2c_def.h
/usr/include/xorg/input.h
/usr/include/xorg/inputstr.h
/usr/include/xorg/list.h
/usr/include/xorg/mi.h
/usr/include/xorg/micmap.h
/usr/include/xorg/micoord.h
/usr/include/xorg/migc.h
/usr/include/xorg/miline.h
/usr/include/xorg/mioverlay.h
/usr/include/xorg/mipict.h
/usr/include/xorg/mipointer.h
/usr/include/xorg/mipointrst.h
/usr/include/xorg/misc.h
/usr/include/xorg/miscstruct.h
/usr/include/xorg/mistruct.h
/usr/include/xorg/misync.h
/usr/include/xorg/misyncfd.h
/usr/include/xorg/misyncshm.h
/usr/include/xorg/misyncstr.h
/usr/include/xorg/mizerarc.h
/usr/include/xorg/nonsdk_extinit.h
/usr/include/xorg/opaque.h
/usr/include/xorg/optionstr.h
/usr/include/xorg/os.h
/usr/include/xorg/panoramiX.h
/usr/include/xorg/panoramiXsrv.h
/usr/include/xorg/picture.h
/usr/include/xorg/picturestr.h
/usr/include/xorg/pixmap.h
/usr/include/xorg/pixmapstr.h
/usr/include/xorg/present.h
/usr/include/xorg/presentext.h
/usr/include/xorg/privates.h
/usr/include/xorg/property.h
/usr/include/xorg/propertyst.h
/usr/include/xorg/ptrveloc.h
/usr/include/xorg/randrstr.h
/usr/include/xorg/region.h
/usr/include/xorg/regionstr.h
/usr/include/xorg/registry.h
/usr/include/xorg/resource.h
/usr/include/xorg/rgb.h
/usr/include/xorg/rrtransform.h
/usr/include/xorg/sarea.h
/usr/include/xorg/screenint.h
/usr/include/xorg/scrnintstr.h
/usr/include/xorg/selection.h
/usr/include/xorg/servermd.h
/usr/include/xorg/shadow.h
/usr/include/xorg/shadowfb.h
/usr/include/xorg/shmint.h
/usr/include/xorg/syncsdk.h
/usr/include/xorg/validate.h
/usr/include/xorg/vbe.h
/usr/include/xorg/vbeModes.h
/usr/include/xorg/vgaHW.h
/usr/include/xorg/vndserver.h
/usr/include/xorg/wfbrename.h
/usr/include/xorg/window.h
/usr/include/xorg/windowstr.h
/usr/include/xorg/xaarop.h
/usr/include/xorg/xace.h
/usr/include/xorg/xacestr.h
/usr/include/xorg/xf86-input-inputtest-protocol.h
/usr/include/xorg/xf86.h
/usr/include/xorg/xf86Crtc.h
/usr/include/xorg/xf86Cursor.h
/usr/include/xorg/xf86DDC.h
/usr/include/xorg/xf86MatchDrivers.h
/usr/include/xorg/xf86Modes.h
/usr/include/xorg/xf86Module.h
/usr/include/xorg/xf86Opt.h
/usr/include/xorg/xf86Optionstr.h
/usr/include/xorg/xf86Optrec.h
/usr/include/xorg/xf86Parser.h
/usr/include/xorg/xf86Pci.h
/usr/include/xorg/xf86PciInfo.h
/usr/include/xorg/xf86Priv.h
/usr/include/xorg/xf86Privstr.h
/usr/include/xorg/xf86RandR12.h
/usr/include/xorg/xf86VGAarbiter.h
/usr/include/xorg/xf86Xinput.h
/usr/include/xorg/xf86_OSlib.h
/usr/include/xorg/xf86_OSproc.h
/usr/include/xorg/xf86cmap.h
/usr/include/xorg/xf86fbman.h
/usr/include/xorg/xf86i2c.h
/usr/include/xorg/xf86int10.h
/usr/include/xorg/xf86platformBus.h
/usr/include/xorg/xf86sbusBus.h
/usr/include/xorg/xf86str.h
/usr/include/xorg/xf86xv.h
/usr/include/xorg/xf86xvmc.h
/usr/include/xorg/xf86xvpriv.h
/usr/include/xorg/xisb.h
/usr/include/xorg/xkbfile.h
/usr/include/xorg/xkbrules.h
/usr/include/xorg/xkbsrv.h
/usr/include/xorg/xkbstr.h
/usr/include/xorg/xorg-server.h
/usr/include/xorg/xorgVersion.h
/usr/include/xorg/xserver-properties.h
/usr/include/xorg/xserver_poll.h
/usr/include/xorg/xvdix.h
/usr/include/xorg/xvmcext.h
/usr/lib64/pkgconfig/xorg-server.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/xorg/modules/drivers/modesetting_drv.so
/V3/usr/lib64/xorg/modules/extensions/libglx.so
/V3/usr/lib64/xorg/modules/input/inputtest_drv.so
/V3/usr/lib64/xorg/modules/libexa.so
/V3/usr/lib64/xorg/modules/libfbdevhw.so
/V3/usr/lib64/xorg/modules/libglamoregl.so
/V3/usr/lib64/xorg/modules/libint10.so
/V3/usr/lib64/xorg/modules/libshadow.so
/V3/usr/lib64/xorg/modules/libshadowfb.so
/V3/usr/lib64/xorg/modules/libvgahw.so
/V3/usr/lib64/xorg/modules/libwfb.so
/usr/lib64/xorg/modules/drivers/modesetting_drv.so
/usr/lib64/xorg/modules/extensions/libglx.so
/usr/lib64/xorg/modules/input/inputtest_drv.so
/usr/lib64/xorg/modules/libexa.so
/usr/lib64/xorg/modules/libfbdevhw.so
/usr/lib64/xorg/modules/libglamoregl.so
/usr/lib64/xorg/modules/libint10.so
/usr/lib64/xorg/modules/libshadow.so
/usr/lib64/xorg/modules/libshadowfb.so
/usr/lib64/xorg/modules/libvgahw.so
/usr/lib64/xorg/modules/libwfb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xorg-server/11d1ae389a1a78f7832586e4c2a0c3c7263b7475

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/Xnest.1
/usr/share/man/man1/Xorg.1
/usr/share/man/man1/Xserver.1
/usr/share/man/man1/Xvfb.1
/usr/share/man/man1/gtf.1
/usr/share/man/man4/exa.4
/usr/share/man/man4/fbdevhw.4
/usr/share/man/man4/inputtestdrv.4
/usr/share/man/man4/modesetting.4
/usr/share/man/man5/xorg.conf.5
/usr/share/man/man5/xorg.conf.d.5

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/Xorg
