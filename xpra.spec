Summary:	Persistent remote applications for X
Name:		xpra
Version:	4.2.3
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		http://xpra.org/
Source0:	http://xpra.org/src/%{name}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	python-cython
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(py3cairo)
#BuildRequires:	pkgconfig(pycairo)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(vpx)
BuildRequires:	typelib(GObject)
BuildRequires:	typelib(Gdk)
BuildRequires:	typelib(GdkPixbuf)
BuildRequires:	typelib(GdkX11)
BuildRequires:	typelib(Gtk) = 3.0
BuildRequires:	typelib(Notify)
BuildRequires:	x11-server-xorg
Requires(pre,postun):	rpm-helper
Requires:	typelib(GObject)
Requires:	typelib(Gdk)
Requires:	typelib(GdkPixbuf)
Requires:	typelib(GdkX11)
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(Notify)
Requires:	x11-tools
Requires:	x11-server-xvfb
Requires:	python-imaging
Requires:	python-dbus

%description
Xpra gives you "persistent remote applications" for X. That is, unlike normal
X applications, applications run with xpra are "persistent" -- you can run
them remotely, and they don't die if your connection does. You can detach them,
and reattach them later -- even from another computer -- with no loss of state.
And unlike VNC or RDP, xpra is for remote applications, not remote desktops --
individual applications show up as individual windows on your screen, managed
by your window manager. They're not trapped in a box. So basically it's screen
for remote X apps.

%pre
%_pre_groupadd xpra

%postun
%_postun_groupdel xpra

%prep
%setup -q

%build
python setup.py build --optimize=1 --skip-build

%install
python setup.py install -O1  --prefix /usr --skip-build --root %{buildroot}

%files
%{_sysconfdir}/%{name}/xpra.conf
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

