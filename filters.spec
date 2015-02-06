%define debug_package %{nil}

Name: filters
Version: 2.48
Release: 3
Summary: A collection of text filters, including the Swedish Chef
License: GPL
Group: Toys
URL: http://kitenet.net/~joey/code/filters.html
# author distributes tarball only from debian pool
Source: http://ftp.debian.org/debian/pool/main/f/filters/filters_2.48.tar.gz
BuildRequires: flex, byacc

%description
A collection of filters to do all sorts of strange things to text.
This includes such favorites as B1FF and the Swedish Chef, and a
wide range of others.

%prep
%setup -q -n %{name}

sed -r -i '/\s+g*cc/s,g*cc,\$(CC),' *.dir/makefile

%build
export CC="%__cc %{optflags}"
%make

%install
%makeinstall_std

%files
%defattr(0644,root,root,0755)
%doc README
%attr(0755,root,root) %{_gamesbindir}/*
%{_mandir}/man6/*


