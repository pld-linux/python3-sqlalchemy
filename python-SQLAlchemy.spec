Summary:	Database Abstraction Library
Name:		python-SQLAlchemy
Version:	0.1.7
Release:	1
Group:		Development/Languages/Python
License:	MIT
Source0:	http://cheeseshop.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
# Source0-md5:	1c9c0124ad057c9fbcf8c4e16ecae960
URL:		http://www.sqlalchemy.org/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python SQL toolkit and Object Relational Mapper that gives application
developers the full power and flexibility of SQL. SQLAlchemy provides a
full suite of well known enterprise-level persistence patterns, designed for
efficient and high-performing database access, adapted into a simple and
Pythonic domain languag.

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

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f \{\} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES doc/*html examples/
%{py_sitescriptdir}/SQLAlchemy*
%{py_sitescriptdir}/sqlalchemy*
