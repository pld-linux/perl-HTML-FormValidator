%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	FormValidator
Summary:	HTML::FormValidator - validate user input, basing on input profile
Summary(pl.UTF-8):	HTML::FormValidator - sprawdzanie w oparciu o schemat, co wprowadził użytkownik
Name:		perl-HTML-FormValidator
Version:	0.11
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	860703094c6d68a3453f3319225066ed
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FormValidator validates user input (usually from an HTML form)
based on an input profile.  It's main aim is to make the tedious
coding of input validation expressible in a simple format and to let
the programmer focus on more interesting task.

%description -l pl.UTF-8
HTML::FormValidator sprawdza poprawność otrzymanych od użytkownika
danych, w oparciu o zdefiniowany profil. Głównym celem jest
uproszczenie nudnego procesu kodowania kontroli poprawności danych
wejściowych i pozwolenie programiście na koncentrację na bardziej
interesujących zadaniach.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
