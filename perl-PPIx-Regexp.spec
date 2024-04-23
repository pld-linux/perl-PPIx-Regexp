#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	PPIx
%define		pnam	Regexp
Summary:	PPIx::Regexp - represent a regular expression of some sort
Summary(pl.UTF-8):	PPIx::Regexp - reprezentacja pewnego rodzaju wyrażenia regularnego
Name:		perl-PPIx-Regexp
Version:	0.050
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/W/WY/WYANT/PPIx-Regexp-%{version}.tar.gz
# Source0-md5:	512573bd4c597e96ce07ff11d50a7df6
URL:		http://search.cpan.org/dist/PPIx-Regexp/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-PPI >= 1.117
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package parses regular expressions as they appear in Perl
scripts, generating a structure similar to the structure generated by
PPI when it parses a Perl script, and navigable in much the same way.

%description -l pl.UTF-8
Ten pakiet analizuje wyrażenia regularne w takiej postaci, w jakiej
występują w skryptach perlowych, tworząc strukturę podobną do
struktury generowanej przez PPI przy analizie skryptu perlowego i
dającą się przeglądać w bardzo podobny sposób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/preslurp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PPIx/Regexp.pm
%{perl_vendorlib}/PPIx/Regexp
%{_mandir}/man3/PPIx::Regexp*.3pm*
%{_examplesdir}/%{name}-%{version}
