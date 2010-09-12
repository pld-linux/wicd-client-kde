
%define		qtver	    	4.6.3

Summary:	KDE4 WicdClient
Summary(pl.UTF-8):	KDE4 WicdClient
Name:		wicd-client-kde
Version:	0.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	http://kde-apps.org/CONTENT/content-files/132366-%{name}_%{version}.tar.gz
# Source0-md5:	79b41039ea840f6f4d1d17d62de25873
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wicd Client KDE is a Wicd client build on the KDE Development
Platform.

%description -l pl.UTF-8
Client Wicd napisany dla środowiska KDE.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wicd-client-kde
%attr(755,root,root) %{_libdir}/kde4/libexec/wicdclient_scripts_helper
%{_desktopdir}/kde4/wicd-client-kde.desktop
%{_datadir}/autostart/wicd-client-kde.desktop
%{_datadir}/dbus-1/system-services/org.kde.wicdclient.scripts.service
%{_datadir}/polkit-1/actions/org.kde.wicdclient.scripts.policy
%{_sysconfdir}/dbus-1/system.d/org.kde.wicdclient.scripts.conf
