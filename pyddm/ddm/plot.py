from .model import *
import matplotlib.pyplot as plt

def plot_solution_pdf(sol, ax=None, correct=True):
    """Plot the PDF of the solution.

    - `ax` is optionally the matplotlib axis on which to plot.
    - If `correct` is true, we draw the distribution of correct
      answers.  Otherwise, we draw the error distributions.

    This does not return anything, but it plots the PDF.  It does not
    show it, and thus requires a call to plt.show() to see.
    """
    if ax == None:
        ax = plt.gca()

    if correct == True:
        ts = sol.pdf_corr()
    else:
        ts = sol.pdf_err()
    
    ax.plot(sol.model.t_domain(), ts, label=sol.model.name)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('PDF (normalized)')
    
def plot_solution_cdf(sol, ax=None, correct=True):
    """Plot the CDF of the solution.

    - `ax` is optionally the matplotlib axis on which to plot.
    - If `correct` is true, we draw the distribution of correct
      answers.  Otherwise, we draw the error distributions.

    This does not return anything, but it plots the CDF.  It does not
    show it, and thus requires a call to plt.show() to see.
    """
    if ax == None:
        ax = plt.gca()

    if correct == True:
        ts = sol.cdf_corr()
    else:
        ts = sol.cdf_err()
    
    ax.plot(sol.model.t_domain(), ts, label=sol.model.name)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('CDF (normalized)')
    
def plot_fit_diagnostics(model, rt_data_corr, rt_data_err):
    """Compare actual data to the best fit model of the data.

    - `model` should be the Model object fit from `rt_data`.
    - `rt_data_corr` should be a list of reaction times for correct trials
    - `rt_data_err` should be a list of reaction times for error trials
    """
    T_dur = model.T_dur
    dt = model.dt
    data_hist_corr = np.histogram(rt_data_corr, bins=T_dur/dt+1, range=(0-dt/2, T_dur+dt/2))[0] # dt/2 terms are for continuity correction
    data_hist_err = np.histogram(rt_data_err, bins=T_dur/dt+1, range=(0-dt/2, T_dur+dt/2))[0]
    total_samples = len(rt_data_corr) + len(rt_data_err)
    sol = model.solve()
    plt.subplot(2, 1, 1)
    plt.plot(model.t_domain(), data_hist_corr/total_samples/dt) # Divide by samples and dt to scale to same size as solution pdf
    plt.plot(model.t_domain(), sol.pdf_corr())
    plt.subplot(2, 1, 2)
    plt.plot(model.t_domain(), data_hist_err/total_samples/dt)
    plt.plot(model.t_domain(), sol.pdf_err())
