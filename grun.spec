Summary:	gRun is an advanced application launcher written in C and GTK
Summary(pl):	gRun jest zaawansowanym launcher'em do aplikacji napisanych w C i GTK
Name:		grun
Version:	0.9.2
Release:	2
License:	GPL
Vendor:		Bruce Smith <tangomanrulz@geocities.com>
Group:		X11/Applications
Source0:	http://www.geocities.com/ResearchTriangle/Facility/1468/sg/%{name}-%{version}.tar.gz
URL:		http://www.geocities.com/ResearchTriangle/Facility/1468/sg/grun.html
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.1.2
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Welcome to gRun, an advanced application launcher written in C and
using GTK for the interface. gRun includes features such as a history,
command completion from the history and from PATH, recognition of
console mode applications and launching a terminal for them, file
extension associations and a dual fork()/execvp() application
launcher.

%description -l pl
Witamy w gRun, zaawansowanym "odpalaczu" aplikacji napisanych w C oraz
u¿ywaj±ca interfejsu GTK. gRun daje takie udogodnienia jak historia,
uzupe³nianie komend z historii i ze ¶cie¿ki, rozpoznawanie aplikacji
uruchamianych w konsoli, a tak¿e teraminal dla nich, kojarzenie z
rozszerzeniami plików i podwójny fork()/execvp() launcher aplikacji.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-associations
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/grun
%{_mandir}/man1/*
%{_datadir}/grun
