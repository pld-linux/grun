%define name grun
%define version 0.8.0
%define release 1
%define serial 1

Summary: gRun is an advanced application launcher written in C and GTK.
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: %{serial}
Copyright: GPL
Group: X11/Utilities
URL: http://www.geocities.com/ResearchTriangle/Facility/1468/sg/index.html
Vendor: Bruce Smith <tangomanrulz@geocities.com>
Source: %{name}-%{version}.tar.gz
Distribution: Freshmeat RPMs
Requires: gtk+ >= 1.1.2
Packager: Ryan Weaver <ryanw@infohwy.com>
BuildRoot: /tmp/%{name}-%{version}

%description
Welcome to gRun, an advanced application launcher written in C and using
GTK for the interface. gRun includes features such as a history, command
completion from the history and from PATH, recognition of console mode
applications and launching a terminal for them, file extension associations
and a dual fork()/execvp() application launcher.

%prep
%setup -q
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr/X11R6 --enable-associations

%build
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL INSTALL.Win NEWS README TODO
%attr(755,root,root) /usr/X11R6/bin/grun
%attr(644,root,root) /usr/X11R6/man/man1/grun.1x
%attr(755,root,root) /usr/X11R6/share/grun

%changelog
* Sat Dec 19 1998 Ryan Weaver <ryanw@infohwy.com>
  [grun-0.8.0-1]
- First RPM
- gRun-0.8.0 Released
