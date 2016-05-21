Summary:	Persistent remote applications for X
Name:		xpra
Version:	0.17.1
Release:	0.2
License:	GPLv2+
Group:		Networking/Other
URL:		http://xpra.org/
Source0:	http://xpra.org/src/%{name}-%{version}.tar.xz
#Patch0:		xpra-0.16.2-compile.patch
BuildRequires:	python-setuptools
BuildRequires:	python-cython
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
Requires:	pygtk2.0
Requires:	x11-tools
Requires:	x11-server-xvfb
Requires:	python-imaging
Requires:	python-dbus
Requires:	python-opencv
Requires:	python-lzo
Requires:	python-opengl

%description
Xpra gives you "persistent remote applications" for X. That is, unlike normal
X applications, applications run with xpra are "persistent" -- you can run
them remotely, and they don't die if your connection does. You can detach them,
and reattach them later -- even from another computer -- with no loss of state.
And unlike VNC or RDP, xpra is for remote applications, not remote desktops --
individual applications show up as individual windows on your screen, managed
by your window manager. They're not trapped in a box. So basically it's screen
for remote X apps.

%prep
%setup -q
%apply_patches

# fix check of python imaging version
sed -i 's/PIL.PILLOW_VERSION/Image.VERSION/' xpra/codecs/pillow/{encode,decode,__init__}.py

%build
python setup.py build --without-enc_x264 build_ext --libraries X11 build_ext -lm

%install
python setup.py install -O1  --prefix /usr --skip-build --root %{buildroot} 

%files
%{_sysconfdir}/%{name}/xpra.conf
%{_sysconfdir}/%{name}/xorg.conf
%{_bindir}/xpra*
%{_iconsdir}/%{name}.png
%{_datadir}/applications/xpra_launcher.desktop
%{py_platsitedir}/xpra
%{py_platsitedir}/xpra-*.egg-info
%{_datadir}/xpra
%{_datadir}/applications/xpra.desktop
%{_mandir}/man1/xpra.1.*
%{_mandir}/man1/xpra_launcher.1.*
%{_prefix}/lib/cups/backend/xpraforwarder
%{_prefix}/lib/tmpfiles.d/xpra.conf
%{_datadir}/appdata/xpra.appdata.xml
%{_datadir}/mime/packages/application-x-xpraconfig.xml

