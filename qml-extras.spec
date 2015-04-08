%define debug_package %nil
%define snap	20150408

Summary:	QML Extras
Name:		qml-extras
Version:	0.0.0
Release:	1.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/qml-extras
# git clone https://github.com/papyros/qml-extras.git
# git archive --format=tar --prefix qml-extras-0.0.0-$(date +%Y%m%d)/ HEAD | xz -vf > qml-extras-0.0.0-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Quick)

%description
Extra types and utilities to make QML even more awesome.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_qt5_libdir}/qt5/qml/Material/*
%{_qt5_libdir}/qt5/tests/tst_extras/tst_extras
