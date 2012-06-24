Summary:	Rhino - JavaScript for Java
Summary(pl):	Rhino - JavaScript dla Javy
Name:		rhino
# TODO: with next version don't put "R1" to Version (to avoid epoch bumps!)
Version:	1.6R2
%define	fver	%(echo %{version} | tr . _)
Release:	1
License:	NPL 1.1
Group:		Development/Languages/Java
Source0:	http://ftp.mozilla.org/pub/mozilla.org/js/%{name}%{fver}.zip
# Source0-md5:	ecbf70d0d4f68e75d90ccf4a6a391b99
URL:		http://www.mozilla.org/rhino/
#BuildRequires:	jakarta-ant
BuildRequires:	unzip
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%description -l pl
Rhino to implementacja JavaScriptu z otwartymi �r�d�ami napisana
ca�kowicie w Javie. Zwykle jest osadzana w aplikacjach w Javie aby
pozwoli� u�ytkownikom na u�ywanie skrypt�w.

%prep
%setup -q -n %{name}%{fver}

%build
# tries to download xbean.zip from www.apache.org
#ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install js.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_javalibdir}/*.jar
