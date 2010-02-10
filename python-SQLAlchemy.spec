%define		module  SQLAlchemy
%define		_beta	beta1
Summary:	Database Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych
Name:		python-%{module}
Version:	0.6
Release:	0.%{_beta}.1
License:	MIT
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/sqlalchemy/%{module}-%{version}%{_beta}.tar.gz
# Source0-md5:	b283b2799804d49c45d44a62da594f7b
URL:		http://www.sqlalchemy.org/
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-setuptools >= 0.6-0.a9.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

%description -l pl.UTF-8
Zestaw narzędzi SQL dla Pythona oraz odwzorowań obiektowo-relacyjnych
dających programistom całą potęgę i elastyczność SQL-a. SQLAlchemy
udostępnia pełny zbiór dobrze znanych wzorców trwałości,
zaprojektowanych do wydajnego dostępu do baz danych, zaadoptowanych do
prostej, pythonowej domeny językowej.

%prep
%setup -q -n %{module}-%{version}%{_beta}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* doc/*.html
%{py_sitescriptdir}/SQLAlchemy*
%{py_sitescriptdir}/sqlalchemy*
%{_examplesdir}/%{name}-%{version}
