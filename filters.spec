
%define name	filters
%define version	2.46
%define rel	1
%define release %mkrel %rel

Name: %name
Version: %version
Release: %release
Summary: A collection of text filters, including the Swedish Chef
License: GPL
Group: Toys
URL: http://kitenet.net/~joey/code/filters.html
# author distributes tarball only from debian pool
Source: http://ftp.debian.org/debian/pool/main/f/filters/%{name}_%{version}.tar.gz
Patch0: filters-printf-format.patch
BuildRequires: flex, byacc
BuildRoot: %{_tmppath}/%{name}-root

%description
A collection of filters to do all sorts of strange things to text.
This includes such favorites as B1FF and the Swedish Chef, and a
wide range of others.

%prep
%setup -q -n %{name}
%patch0 -p1

sed -r -i '/\s+g*cc/s,g*cc,\$(CC),' *.dir/makefile

%build
export CC="%__cc %optflags"
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README
%attr(0755,root,root) %{_gamesbindir}/*
%{_mandir}/man6/*
