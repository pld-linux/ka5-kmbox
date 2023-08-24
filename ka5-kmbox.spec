#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmbox
Summary:	Kmbox
Name:		ka5-%{kaname}
Version:	23.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d2229d6010dd7ba976276ff1a769ce59
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides support for mail apps.

%description -l pl.UTF-8
Biblioteka ze wsparciem dla programów pocztowych.

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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_datadir}/qlogging-categories5/kmbox.categories
%{_datadir}/qlogging-categories5/kmbox.renamecategories
%ghost %{_libdir}/libKPim5Mbox.so.5
%attr(755,root,root) %{_libdir}/libKPim5Mbox.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/qt5/mkspecs/modules/qt_KMbox.pri
%{_includedir}/KPim5/KMbox
%{_libdir}/cmake/KPim5Mbox
%{_libdir}/libKPim5Mbox.so
