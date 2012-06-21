Name:           kde-plasma-menubar
Version:        0.1.18
Release:        1%{?dist}
Summary:        A Plasma widget to display menubar of application windows

License:        GPLv3
URL:            https://launchpad.net/plasma-widget-menubar
Source0:        https://launchpad.net/plasma-widget-menubar/trunk/%{version}/+download/plasma-widget-menubar-%{version}.tar.bz2

BuildRequires:  kdelibs-devel
BuildRequires:  dbusmenu-qt-devel
BuildRequires:  qjson-devel

%description
Plasma widget to display menubar of application windows

%prep
%setup -q -n plasma-widget-menubar-%{version}


%build
%{cmake_kde4} .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING NEWS
%{_kde4_libdir}/kde4/plasma_applet_menubar.so
%{_kde4_datadir}/kde4/services/plasma-applet-menubar.desktop


%changelog
* Thu Jun 21 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.1.18-1.R
- initial build