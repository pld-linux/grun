Summary:	gRun is an advanced application launcher written in C and GTK
Name:		grun
Version:	0.9.2
Release:	1
License:	GPL
Vendor:		Bruce Smith <tangomanrulz@geocities.com>
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.geocities.com/ResearchTriangle/Facility/1468/sg/%{name}-%{version}.tar.gz
URL:		http://www.geocities.com/ResearchTriangle/Facility/1468/sg/grun.html
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Welcome to gRun, an advanced application launcher written in C and
using GTK for the interface. gRun includes features such as a history,
command completion from the history and from PATH, recognition of
console mode applications and launching a terminal for them, file
extension associations and a dual fork()/execvp() application
launcher.

%prep
%setup -q

%build
gettextize --copy --force
%configure \
	--enable-associations
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/grun
%{_mandir}/man1/*
%{_datadir}/grun
