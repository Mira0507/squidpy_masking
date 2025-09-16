#' Print Python subchunks
#'
#' This function generates subchunks running Python scripts. Python code is 
#' flexibly provided using the `t_deparsed` argument.
#'
#' @param name string chunk name
#' @param t_deparsed the vector of strings
#' @param width integer the width of image 
#' @param height integer the height of image
#'
#' @return string concatenated and printed chunk with Python code
subchunkify <- function(name, t_deparsed, width=12, height=12) {

    more <- paste0(", fig.width=", width, ", fig.height=", height)
    sub_chunk <- paste0("```{python ", name, ", results='asis', echo=FALSE", more, "}",
        "\n\n",
        paste0(t_deparsed, collapse="\n"),
        "\n\n```\n\n\n")

    cat(knitr::knit(text = sub_chunk, quiet=TRUE))
}

##' Provide a link to a file path
#'
#' This function generates a link to a file path 
#'
#' @param p string a path to desired file
#'
#' @return link
link_output <- function(p) {
    cat("\n\n- Link: [", p, "](", p, ")\n\n")
}
