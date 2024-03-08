# Run tests in check section
%bcond_without check

# https://github.com/google/renameio
%global goipath		github.com/google/renameio
%global forgeurl	https://github.com/google/renameio
Version:		1.0.0

%gometa

Summary:	A way to atomically create or replace a file or symbolic link
Name:		golang-github-google-renameio

Release:	1
Source0:	https://github.com/google/renameio/archive/v%{version}/renameio-%{version}.tar.gz
URL:		https://github.com/google/renameio
License:	ASL 2.0
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
This Go package provides a way to atomically create o
replace a file or symbolic link.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n renameio-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

