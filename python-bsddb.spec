%bcond_without	python2
%bcond_without	python3
#
%define		pname	bsddb3
%define		module	bsddb
Summary:	Python interface for BerkeleyDB
Summary(pl.UTF-8):	Interfejs Pythona do BerkeleyDB
Name:		python-%{module}
Version:	5.1.2
Release:	1
License:	BSD-like w/o adv. clause
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/b/bsddb3/%{pname}-%{version}.tar.gz
# Source0-md5:	39a6b87af22318e2ff00b0c1b15c627c
URL:		http://www.argo.es/~jcea/programacion/pybsddb.htm
BuildRequires:	db-devel >= 4.1.25
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Obsoletes:	bsddb3
Obsoletes:	python-bsddb3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a nearly complete wrapping of the Sleepycat C API
for the Database Environment, Database, Cursor, and Transaction
objects, and each of these is exposed as a Python Type in the
bsddb3.db module. The databse objects can use various access methods:
btree, hash, recno, and queue. For the first time all of these are
fully supported in the Python wrappers. Please see the documents in
the docs directory of the source distribution or at the website for
more details on the types and methods provided.

%description -l pl.UTF-8
Ten moduł dostarcza prawie całkowite opakowanie API C Sleepycat do
obiektów środowiska baz danych, baz danych, kursorów i transakcji, z
których każdy jest udostępniony jako pythonowy typ w module bsddb3.db.
Obiekty bazy danych mogą używać różnych metod dostępu: btree, hash,
recno i queue. Jest to pierwsza implementacja obsługi tych obiektów
dla Pythona. Więcej szczegółów o typach i metodach znajduje się w
załączonej dokumentacji lub na stronie WWW.

%package -n python3-%{pname}
Summary:	Python interface for BerkeleyDB
Summary(pl.UTF-8):	Interfejs Pythona do BerkeleyDB
Group:		Development/Languages/Python

%description -n python3-%{pname}
This module provides a nearly complete wrapping of the Oracle C API
for the Database Environment, Database, Cursor, and Transaction
objects, and each of these is exposed as a Python Type in the
bsddb3.db module. The databse objects can use various access methods:
btree, hash, recno, and queue. For the first time all of these are
fully supported in the Python wrappers. Please see the documents in
the docs directory of the source distribution or at the website for
more details on the types and methods provided.

%description -n python3-%{pname} -l pl.UTF-8
Ten moduł dostarcza prawie całkowite opakowanie API C Oracle do
obiektów środowiska baz danych, baz danych, kursorów i transakcji, z
których każdy jest udostępniony jako pythonowy typ w module bsddb3.db.
Obiekty bazy danych mogą używać różnych metod dostępu: btree, hash,
recno i queue. Jest to pierwsza implementacja obsługi tych obiektów
dla Pythona. Więcej szczegółów o typach i metodach znajduje się w
załączonej dokumentacji lub na stronie WWW.

%prep
%setup -q -n %{pname}-%{version}

%build
%if %{with python2}
env CFLAGS="%{rpmcflags}" \
%{__python} setup.py build -b build-2 \
	--berkeley-db-libdir=%{_libdir} \
	--berkeley-db=%{_prefix}
%endif

%if %{with python3}
env CFLAGS="%{rpmcflags}" \
%{__python3} setup.py build -b build-3 \
	--berkeley-db-libdir=%{_libdir} \
	--berkeley-db=%{_prefix}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py build -b build-2 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2 \

%py_postclean

# do not include in main package tests and devel headers
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bsddb3/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/bsddb3/test_support.*
%{__rm} -r $RPM_BUILD_ROOT%{py_incdir}/bsddb3/bsddb.h
%endif

%if %{with python3}
%{__python3} setup.py build -b build-3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2 \

%py3_postclean
# do not include in main package tests and devel headers
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bsddb3/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/bsddb3/test_support.*
%{__rm} -r $RPM_BUILD_ROOT%{py3_incdir}/bsddb3/bsddb.h
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc *.txt
%dir %{py_sitedir}/bsddb3
%{py_sitedir}/bsddb3/*.py[co]
%attr(755,root,root) %{py_sitedir}/bsddb3/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/bsddb3-*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{pname}
%defattr(644,root,root,755)
%doc *.txt docs
%dir %{py3_sitedir}/bsddb3
%{py3_sitedir}/*.egg-info
%{py3_sitedir}/bsddb3/*.py[co]
%attr(755,root,root) %{py3_sitedir}/bsddb3/*.so
%endif
