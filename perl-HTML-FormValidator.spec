%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	FormValidator
Summary:	Validate user input, basing on input profile
Summary(pl):	Sprawd¼ to, co wprowadzi³ u¿ytkownik w oparciu o schemat
Name:		perl-%{pdir}-%{pnam}
Version:	0.11
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FormValidator validates user input (usually from an HTML form)
based on an input profile.  It's main aim is to make the tedious coding of
input validation expressible in a simple format and to let the programmer
focus on more interesting task.

%description -l pl
HTML::FormValidator sprawdza poprawno¶æ otrzymanych od u¿ytkownika danych,
w oparciu o zdefiniowany profil.  G³ównym celem jest uproszczenie nudnego
procesu kodowania kontroli poprawno¶ci danych wej¶ciowych i pozwolenie
programi¶cie na koncentracjê na bardziej interesuj±cych zadaniach.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
