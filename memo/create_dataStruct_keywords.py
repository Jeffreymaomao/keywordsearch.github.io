import random
import hashlib
import json 

keys = [
	"Absolute Zero of Temperature",
	"Absorbed Dose (D)",
	"Acceleration (a)",
	"Accuracy",
	"Acoustic Impedance (Z)",
	"Active Solar Heater (solar panel)",
	"Activity (A)",
	"Adiabatic",
	"Albedo (α)",
	"Alpha Particle (α)",
	"Amplitude",
	"Analog",
	"Analyzer",
	"Angular magnification",
	"Antinode",
	"Artificial (Induced) Transmutation",
	"A-scan",
	"Asia-Pacific Partnership on Clean Development and Climate (APPCDC)",
	"Attenuation",
	"Attenuation Coefficient (μ)",
	"Avogadro constant (NA)",
	"Bainbridge Mass Spectrometer",
	"Balanced Risk",
	"Beta Negative Particle (β–)",
	"Beta Positive Particle (β+)",
	"Binary Number",
	"Binding Energy",
	"Binding Energy per Nucleon",
	"per nucleon",
	"per nucleon",
	"Biological Half-life (TB)",
	"Bit",
	"Black-Body Radiation",
	"Boiling",
	"Brewster’s Law",
	"B-scan",
	"Bumps and Pits",
	"Byte",
	"Capacitance (C)",
	"Chain Reaction",
	"Change in Gravitational Potential Energy (ΔEp)",
	"Charge-Coupled Device (CCD)",
	"Chromatic aberration",
	"Coefficient of Volume Expansion (γ)",
	"Compression",
	"Computed Tomography (CT) Scan",
	"Conductor",
	"Constructive Interference",
	"Control Rods",
	"Controlled Nuclear Fission",
	"Coulomb interaction (Coulomb force, electrostatic force)",
	"Coulomb’s Law",
	"Crest",
	"Critical Damping",
	"Critical Mass",
	"Damping",
	"Davisson-Germer Experiment",
	"de Broglie Hypothesis",
	"λ = h/p",
	"Decimal Number",
	"Degraded Energy",
	"Derived Units",
	"Destructive Interference",
	"Diffraction",
	"Digital",
	"Dioptre",
	"Direction of a Magnetic Field",
	"Dispersion",
	"Displacement (for waves)",
	"Displacement (s)",
	"Doppler Effect",
	"Dose Equivalent (H)",
	"Effective Half-life (TE)",
	"Efficiency (eff)",
	"Elastic Collision",
	"kinetic",
	"Electric Current (I)",
	"Electric Field Strength (E)",
	"Electric Potential (V)",
	"Electric Potential Difference (ΔV)",
	"Electric Potential Energy (Ee)-",
	"Electromotive Force (emf) (ε)",
	"Electron in a Box Model",
	"Electronvolt (eV)",
	"Emissivity (ε)",
	"Endoscope",
	"Energy Density (of a fuel)",
	"Enhanced (Anthropogenic) Greenhouse Effect",
	"Entropy",
	"Equipotential Surface",
	"Escape Speed (v­­esc)",
	"Evaporation",
	"Exposure (X)",
	"Far point",
	"Faraday’s Law",
	"Field",
	"(Field of Force)",
	"First Law of Thermodynamics (Q = ΔU + W)",
	"Focal length",
	"Focal point",
	"Forced Oscillations",
	"Fossil Fuels",
	"Frequency (f)",
	"Fuel",
	"Fuel Enrichment",
	"Fundamental (First Harmonic)",
	"Fundamental Units",
	"Gamma Radiation (γ)",
	"Geiger-Marsden experiment",
	"Global Warming",
	"Gravitational Field Strength (g)",
	"Gravitational Potential (V)",
	"Gravitational Potential Energy (EP)",
	"Greenhouse Effect",
	"Half-Value Thickness (x1/2)",
	"Heat Exchanger",
	"Heisenberg Uncertainty Principle",
	"Ideal Ammeter",
	"Ideal Gas",
	"Ideal Voltmeter",
	"Impedance Matching",
	"Impulse (J)",
	"Inelastic Collision",
	"kinetic",
	"not",
	"Inner Ear (especially Cochlea)",
	"Insulator",
	"not",
	"Insulator",
	"not",
	"Intensity (I)",
	"Intergovernmental Panel on Climate Change (IPCC)",
	"Internal Energy of a substance (U)",
	"Internal Resistance (r)",
	"Isobaric",
	"Isochoric (Isovolumetric)",
	"Isothermal",
	"Isotope",
	"Kelvin scale of Temperature",
	"Kepler’s Third Law",
	"Kinetic Energy (EK)",
	"Kyoto Protocol",
	"Law of Conservation of Electric Charge",
	"Law of Conservation of Linear Momentum",
	"Law of Reflection",
	"Least-Significant Bit (LSB)",
	"Lenz’s Law",
	"Light-Dependent Resistor (LDR)",
	"Linear magnification",
	"Linear Momentum (p)",
	"Longitudinal Wave",
	"Loudness",
	"Magnetic Flux (Φ)",
	"normal",
	"Magnetic Flux Linkage",
	"Magnification",
	"Magnitude of a Magnetic Field (magnetic field strength, magnetic field intensity, magnetic flux density) (B)",
	"Malus’ Law",
	"Mass Defect",
	"Matter Waves",
	"Middle Ear",
	"Millikan’s Stopping Potential Experiment",
	"Moderator",
	"Molar Mass",
	"Mole",
	"Monochromatic",
	"Most-Significant Bit (MSB)",
	"Natural Frequency of Vibration",
	"Near point",
	"Negative Temperature Coefficient (NTC) Thermistor",
	"Neutron Number (N)",
	"Newton’s First Law of Motion",
	"Newton’s Second Law of Motion",
	"Newton’s Third Law of Motion",
	"Newton’s Universal Law of Gravitation",
	"Node",
	"Non-Ohmic Device",
	"Non-renewable Energy Source",
	"can",
	"Nuclear Fission",
	"Nuclear Fusion",
	"Nuclear Magnetic Resonance (NMR) Imaging",
	"Nucleon",
	"not",
	"Nucleon Number (Mass Number) (A)",
	"Nuclide",
	"Ohm’s Law",
	"not",
	"Ohmic Device",
	"Optically Active Substance",
	"Oscillating Water Column (OWC) Ocean-Wave Energy Converter",
	"Ossicles",
	"Outer Ear",
	"Path Difference",
	"Period (T)",
	"Phase Difference",
	"Photoelectric Effect",
	"Photon",
	"Photovoltaic Cell (solar cell, photocell)",
	"Physical Half-life (TP) (same as T1/2)",
	"Piezoelectric Crystals",
	"Pixel",
	"Polarized Light",
	"Polarizer",
	"Potential Divider",
	"Power (P)",
	"Power of a converging lens",
	"Precision",
	"Pressure (P)",
	"Principal axis",
	"Principle of Conservation of Energy",
	"Principle of Superposition",
	"Proton Number (Atomic Number) (Z)",
	"Pulse Oximetry",
	"Quantum Efficiency (of a pixel)",
	"Radial Field",
	"Radiation Dosimetry",
	"Radioactive Decay",
	"random",
	"spontaneous",
	"Random Uncertainty",
	"Rarefaction",
	"Ray",
	"Rayleigh Criterion",
	"Real Gas",
	"not",
	"Real image",
	"Relative Biological Effectiveness (RBE) (or Quality Factor)",
	"Renewable Energy Source",
	"Resistance (R)",
	"Resistor",
	"Resolution",
	"Resonance",
	"Root Mean Square (rms) Value of an Alternating Current (or Voltage)",
	"Sankey Diagram",
	"Scalar",
	"Schrödinger Model of the Atom",
	"Second Law of Thermodynamics",
	"Second Law of Thermodynamics",
	"Selective Frequency Loss",
	"Simple Harmonic Motion (SHM)",
	"and",
	"Snell’s Law",
	"Sound Intensity",
	"Sound Intensity Level (IL)",
	"Specific Heat Capacity (c)",
	"per unit mass",
	"Specific Latent Heat (L)",
	"Speed (u,v)",
	"Spherical aberration",
	"Standing (stationary) wave",
	"not",
	"Stefan-Boltzmann Law",
	"Strain Gauge",
	"Surface Heat Capacity (CS)",
	"Systematic Error",
	"Temperature (T)",
	"Thermal Capacity (C)",
	"Thermal Energy (Heat) (Q)",
	"Thermal Equilibrium",
	"Threshold Frequency (f0)",
	"Tinnitus",
	"Translational Equilibrium",
	"Transverse Wave",
	"Traveling Wave (Progressive Wave, Continuous Wave)",
	"Trough",
	"Tympanic Membrane",
	"Ultrasound Scan",
	"Uncontrolled Nuclear Fission",
	"Unified Atomic Mass Unit",
	"Vector",
	"Velocity (u,v)",
	"Virtual image",
	"Wave Pulse",
	"Wave Speed (v)",
	"Wavefront",
	"Wavelength (λ)",
	"Wave-Particle Duality:",
	"Weightlessness in deep space",
	"Weightlessness in free-fall",
	"Weightlessness in orbital motion",
	"Work Function (Φ)",
	"ENTICED RETAIL LLP",
]



def md5(v): return hashlib.md5(v.encode("utf-8")).hexdigest()

sets = "abcdefghijklmnopqrstuvwxyz"
struct = {}

for t1 in sets:
	for t2 in sets:
		for t3 in sets:
			n = t1 + t2 + t3
			k1 = random.choice(keys) 
			k2 = random.choice(keys)
			k3 = random.choice(keys)
			struct[md5(n)] = {
				"n":n,
				"k":[k1,k2,k3]
			}

with open("k.json", "w") as f: 
    json.dump(struct, f)