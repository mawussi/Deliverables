(TeX-add-style-hook
 "one-sided"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("geometry" "margin=25mm")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "one-sided-tile"
    "article"
    "art12"
    "inputenc"
    "fontenc"
    "lmodern"
    "xcolor"
    "colortbl"
    "graphicx"
    "fancyhdr"
    "geometry"
    "lastpage"
    "url"
    "tabularx"
    "amsmath"
    "amssymb"
    "subcaption")
   (TeX-add-symbols
    "nlafetMajor"
    "nlafetMinor"
    "nlafetTitle"
    "nlafetShortTitle"
    "nlafetMonth"
    "nlafetYear"
    "nlafetScheduledDelivery"
    "nlafetActualDelivery"
    "nlafetVersionMajor"
    "nlafetVersionMinor"
    "nlafetResponsiblePartner"
    "nlafetDisseminationLevel")
   (LaTeX-add-labels
    "sec.introduction"
    "fig.chol_dag"
    "sec.tile"
    "sec.runtime_systems"
    "sec.arch"
    "tab.arch"
    "sec.cholesky"
    "fig.chol_numa"
    "fig.chol_knl_ram"
    "sec.lu"
    "fig.lu_numa"
    "fig.lu_knl_ram"
    "sec.qr"
    "fig.qr_numa"
    "fig.qr_knl_ram"
    "sec.ldlt"
    "fig.ldlt_numa"
    "fig.ldlt_knl_ram"
    "sec.conclusions")
   (LaTeX-add-bibliographies
    "svd_biblio"))
 :latex)

