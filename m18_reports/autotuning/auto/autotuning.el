(TeX-add-style-hook
 "autotuning"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("geometry" "margin=25mm")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "url")
   (TeX-run-style-hooks
    "latex2e"
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
    "amssymb")
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
    "sec.review"
    "sec:opentuner"
    "sec.curvefitting"
    "fig.fit_const"
    "fig.fit_linear"
    "fig.fit_log"
    "fig.fit_step"
    "sec.performance"
    "fig.tuned_gemm"
    "fig.tuned_potrf"
    "fig.tuned_getrf"
    "fig.tuned_geqrf"
    "sec.conclusions")
   (LaTeX-add-bibliographies
    "/home/srelton/MATFUN/Total_Bibliography.bib"))
 :latex)

