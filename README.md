autowalk
========

A tool for generating natural-looking walking animations

Setup and Install
--------

1. Install the Autodesk FBX Python SDK. Go to [autodesk.com/fbx](http://www.autodesk.com/fbx), click on the _Downloads_ link, and download the Python SDK. Follow the instructions contained in the INSTALL file.

2. Install the [Open Dynamics Engine](http://www.ode.org/download.html).

3. Install the [Python wrapper](http://pyode.sourceforge.net) for ODE.

Usage
--------

autowalk takes an FBX file containing a humanoid model, and attempts to estimate its mass and dimensions. From there, it tries to generate a neuro-muscular model approximating the FBX model, and uses machine-learning techniques to build a natural-looking walking animation.

The basic heuristic for what constitutes a "good" walking animation is speed and balance. (We haven't yet developed a good definition for "balance" that the simulation can understand)

```bash
python main.py /path/to/your/fbx/file
```

Roadmap
--------

autowalk doesn't do anything yet. Once we have completed its basic functionality, we *may* look at adding support for variations, including:

- walking under different gravitational fields
- walking while carrying arbitrary objects
- walking over various slopes and types of terrain
- wading through substances of various depths and viscosity
- walking against various wind resistances and drag
- moving upright while being struck by objects of various sizes
- walk/run transitions
- jumping and walk/jump transitions
