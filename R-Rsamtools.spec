%bcond_with bootstrap
%global packname  Rsamtools
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.12.4
Release:          1
Summary:          Binary alignment (BAM), variant call (BCF), or tabix file import
Group:            Sciences/Mathematics
License:          Artistic-2.0 + file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/Rsamtools_1.12.4.tar.gz
Requires:         R-methods R-IRanges R-GenomicRanges R-Biostrings
Requires:         R-utils R-zlibbioc R-rtracklayer R-bitops
%if %{with bootstrap}
Requires:         R-RUnit R-KEGG.db
%else
Requires:         R-ShortRead R-GenomicFeatures R-RUnit R-KEGG.db
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-IRanges R-GenomicRanges R-Biostrings
BuildRequires:    R-utils R-zlibbioc R-rtracklayer R-bitops
%if %{with bootstrap}
BuildRequires:    R-RUnit R-KEGG.db
%else
BuildRequires:    R-ShortRead R-GenomicFeatures R-RUnit R-KEGG.db
%endif

%description
This package provides an interface to the 'samtools', 'bcftools', and
'tabix' utilities (see 'LICENCE') for manipulating SAM (Sequence Alignment
/ Map), binary variant call (BCF) and compressed indexed tab-delimited
(tabix) files.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%if %{without bootstrap}
#%check
#%{_bindir}/R CMD check %{packname}
#%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/usretc
%{rlibdir}/%{packname}/usrlib


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6.3-2
+ Revision: 778891
- Rebuild with proper dependencies

* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6.3-1
+ Revision: 776658
- Import R-Rsamtools
- Import R-Rsamtools



