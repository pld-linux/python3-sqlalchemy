Summary:	Database Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych
Name:		python-SQLAlchemy
Version:	0.3.3
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
# Source0-md5:	1336d87f659944f131f7f2c340e81e02
URL:		http://www.sqlalchemy.org/
BuildRequires:	python-devel
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
%setup -q -n SQLAlchemy-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES doc/*html examples/
%{py_sitescriptdir}/SQLAlchemy*
%{py_sitescriptdir}/sqlalchemy*
