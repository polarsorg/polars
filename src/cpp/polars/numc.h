//
// Created by Linda Uruchurtu on 30/08/2018.
//

#ifndef ZIMMER_NUMC_H
#define ZIMMER_NUMC_H

#include "armadillo"

#include <cmath>
#include <vector>

namespace polars {

    namespace numc {

        bool almost_equal_doubles(double a, double b);

        bool equal(const arma::uvec &lhs, const arma::uvec &rhs);

        bool equal_handling_nans(const arma::vec &lhs, const arma::vec &rhs);

        bool almost_equal_handling_nans(const arma::vec &lhs, const arma::vec &rhs);

        arma::vec arange(double start, double stop, double step = 1.);

        double sum_finite(const arma::vec &series);

        arma::vec triang(int M, bool sym = true);

        arma::vec exponential(int M, double tau = 1., bool sym = true, double center=-1.);

        bool double_is_int(double v);

        arma::vec quantile(const arma::vec &x, const arma::vec &q);

        double quantile(const arma::vec &x, double q);

        arma::vec arctan2(const arma::vec &x, const arma::vec &y);

    } // numc
} // polars

#endif //ZIMMER_NUMC_H