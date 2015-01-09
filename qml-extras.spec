%define debug_package %nil
%define snap 20150109

Summary:	QML Extras
Name:		qml-extras
Version:	0.0.0
Release:	0.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/qml-extras
# git archive --format=tar --prefix=qml-extras-0.0.0-20150109/ HEAD | xz -vf > qml-extras-0.0.0-20150109.tar.xz
Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel

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
