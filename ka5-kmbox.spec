%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kmbox
Summary:	Kmbox
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d318c9f0806795d0a3140f9146720210
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-kmime-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.44.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides support for mail apps.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
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
/etc/xdg/kmbox.categories
/etc/xdg/kmbox.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5Mbox.so.5
%attr(755,root,root) %{_libdir}/libKF5Mbox.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KMbox
%{_includedir}/KF5/kmbox_version.h
%{_libdir}/cmake/KF5Mbox
%attr(755,root,root) %{_libdir}/libKF5Mbox.so
%{_libdir}/qt5/mkspecs/modules/qt_Mbox.pri
