"""
Examples of using the terminal velocity functions.
"""

import chemics as cm

# Parameters
# ---------------------------------------------------------------------------

dp = 0.00016    # particle diameter [m]
mu = 1.8e-5     # gas viscosity [kg/(m s)]
phi = 0.67      # particle sphericity [-]
rhog = 1.2      # gas density [kg/m^3]
rhos = 2600     # particle density [kg/m^3]

# Haider and Levenspiel terminal velocity
# ---------------------------------------------------------------------------

ut_haider = cm.ut_haider(dp, mu, phi, rhog, rhos)

# Ganser terminal velocity
# ---------------------------------------------------------------------------

cd, re, ut_ganser = cm.ut_ganser(dp, mu, phi, rhog, rhos)

# Kunii and Levenspiel terminal velocity
# ---------------------------------------------------------------------------

ut = cm.ut(cd, dp, rhog, rhos)

# Print results
# ---------------------------------------------------------------------------

print(f"""
ut = {ut_haider:.4f} m/s (Haider and Levenspiel)
ut = {ut_ganser:.4f} m/s (Ganser)
ut = {ut:.4f} m/s (Kunii and Levenspiel)
cd = {cd:.4f}
re = {re:.4f}
""")
