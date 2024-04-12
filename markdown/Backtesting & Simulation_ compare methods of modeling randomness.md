## Comparing Methods of Modeling Randomness

### Rolling Window Backtesting:
- **Objective:** Understand risk-return trade-off of an investment strategy.
- **Steps:** Specify hypothesis, determine rules, form portfolio, rebalance periodically, compute performance and risk.
- **Framework:** Use rolling window, fit/calibrate factors, rebalance, track performance.
- **Approaches:** Long/short hedged portfolio, Spearman rank IC.
- **Considerations:** Data coverage, return distribution, factor efficacy, turnover, decay.
- **Behavioral Issues:** Survivorship bias, look-ahead bias.

### Risk Parity:
- **Objective:** Equal risk contribution from each factor/asset in the portfolio.
- **Considerations:** Volatility of each factor, correlations between factors.
- **Challenges:** Skewed returns, fat tails, tail dependence.

### Scenario Analysis:
- **Purpose:** Understand strategy performance in different structural regimes.
- **Method:** Assess strategy under various scenarios.

### Historical Simulation:
- **Method:** Relatively straightforward, uses historical data.
- **Pros:** Simple to perform.
- **Cons:** Relies on historical data distribution for future uncertainty.

### Monte Carlo Simulation:
- **Method:** Sophisticated, choice of statistical distribution crucial.
- **Distribution:** Multivariate normal often used, but may not capture skewness and fat tails.
- **Technique:** Inverse transformation method for simulating random variables.

### Sensitivity Analysis:
- **Purpose:** Explore impact of input variable changes on target variable and risk profiles.
- **Use:** Helps understand limitations of conventional Monte Carlo simulation.
- **Consideration:** Multivariate skewed t-distribution for skewness and kurtosis, but more parameter estimation.

By comparing these methods, investors can choose the most suitable approach based on their model building, portfolio construction process, and the nature of the data they are working with. Each method has its strengths and limitations, and a combination of approaches may provide a more comprehensive understanding of randomness in investment returns.