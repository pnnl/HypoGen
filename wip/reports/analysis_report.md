
Running:
 - get_columns(csv_name=temp_uploaded_data.csv)
 - read_csv_file(csv_name=temp_uploaded_data.csv)


 - Running: get_columns(csv_name=temp_uploaded_data)


 - Running: read_csv_file(csv_name=temp_uploaded_data)

### Analysis

#### Chemical Descriptor: Hydroxyl Group Number

<analysis>
<parameter_name>Hydroxyl Group Number</parameter_name>
<definition>Number of hydroxyl groups (-OH) present in the additive's molecular structure.</definition>
<physical_meaning>Hydroxyl groups are polar and capable of forming hydrogen bonds with water molecules.</physical_meaning>
<influence>Negative correlation (ranges from -0.234 to -0.644). The larger the number of hydroxyls, the less the solubilization.</influence>
<intermolecular_interactions>Hydroxyl groups can form hydrogen bonds with carboxylate, sulfonate, aromatic rings, and ketone groups. This enhances their interaction with water but may hinder the active material's ability to interact with water molecules independently.</intermolecular_interactions>
<chemistry_theories>Hydrogen bonding, solvation theory.</chemistry_theories>
<overall_effect>The presence of more hydroxyl groups in the additives decreases the solubilization of the active material since the hydrogen bonding with water competes with necessary interactions between the active material and water.</overall_effect>
</analysis>

#### Chemical Descriptor: Carboxylic Group Number

<analysis>
<parameter_name>Carboxylic Group Number</parameter_name>
<definition>Number of carboxylic acid groups (-COOH) present in the additive's molecular structure.</definition>
<physical_meaning>Carboxylic groups are polar and acidic, capable of donating hydrogen bonds.</physical_meaning>
<influence>Generally weak positive correlation (ranges from -0.063 to 0.029). The carboxylic group number's influence varies slightly with temperature.</influence>
<intermolecular_interactions>Carboxylic groups can interact with all functional groups via hydrogen bonding and ionic interactions. With carboxylate and sulfonate groups, it forms stronger ionic interactions, potentially aiding in their solubilization.</intermolecular_interactions>
<chemistry_theories>Hydrogen bonding, ionic interactions, pH and pKa relationships.</chemistry_theories>
<overall_effect>The presence of carboxylic groups has a weak positive impact on solubilization. The specific interactions depend on pH-sensitive ionic and hydrogen bonds, which can mediate solvation dynamics favorably.</overall_effect>
</analysis>

#### Chemical Descriptor: Amino Group Number

<analysis>
<parameter_name>Amino Group Number</parameter_name>
<definition>Number of amino groups (-NH2) present in the additive's molecular structure.</definition>
<physical_meaning>Amino groups are basic and polar, capable of forming hydrogen bonds with water molecules.</physical_meaning>
<influence>Generally weak positive correlation (ranges from -0.195 to 0.103).</influence>
<intermolecular_interactions>Amino groups can form hydrogen bonds and ionic interactions with carboxylate, aromatic rings, ketone groups, and especially sulfonate groups.</intermolecular_interactions>
<chemistry_theories>Hydrogen bonding, protonation/deprotonation equilibria.</chemistry_theories>
<overall_effect>Presence of amino groups provides a weak positive influence on solubilization. Their ability to form multiple hydrogen bonds and interact ionically assists in stabilization and solubilization of the active material.</overall_effect>
</analysis>

#### Chemical Descriptor: Carbon Group Number

<analysis>
<parameter_name>Carbon Group Number</parameter_name>
<definition>Number of carbon atoms present in the additive's molecular structure.</definition>
<physical_meaning>Generally contributes to the hydrophobicity or hydrophilicity of the molecule depending on other functional groups attached.</physical_meaning>
<influence>Negative correlation (ranges from -0.146 to -0.685). Higher carbon group number decreases solubilization.</influence>
<intermolecular_interactions>Large numbers of carbon atoms increase hydrophobic interactions, which can disrupt solubility by reducing the additive's affinity for water molecules.</intermolecular_interactions>
<chemistry_theories>Hydrophobic effect in solvation theory.</chemistry_theories>
<overall_effect>More carbon groups decrease solubilization likely due to increased hydrophobic interactions, leading to reduced interactions with water molecules.</overall_effect>
</analysis>

#### Chemical Descriptor: Octanol Water Partition Coefficient

<analysis>
<parameter_name>Octanol Water Partition Coefficient</parameter_name>
<definition>Logarithm of the ratio of a compound's concentration in octanol to its concentration in water (logP).</definition>
<physical_meaning>Measures the hydrophobicity or lipophilicity of a molecule. Higher logP indicates more hydrophobicity.</physical_meaning>
<influence>Positive correlation (ranges from 0.145 to 0.631).</influence>
<intermolecular_interactions>Molecules with high logP values favor hydrophobic interactions. They can partition out of water, thus enhancing the solubility of hydrophobic active materials.</intermolecular_interactions>
<chemistry_theories>Hydrophobic effect, solubility theory.</chemistry_theories>
<overall_effect>Higher logP (more hydrophobic additives) increases active material solubilization in water due to favorable hydrophobic interactions segregating hydrophobic active materials into soluble aggregates.</overall_effect>
</analysis>

#### Chemical Descriptor: Molar Refractivity

<analysis>
<parameter_name>Molar Refractivity</parameter_name>
<definition>Measure of the overall polarizability of a molecule per mole of substance.</definition>
<physical_meaning>Reflects how easily the electron cloud around a molecule can be distorted, which influences molecular interactions and solvency.</physical_meaning>
<influence>Negative correlation (ranges from -0.085 to -0.469).</influence>
<intermolecular_interactions>High molar refractivity indicates strong dispersion forces, which may reduce solubilization efficiency in polar solvents like water.</intermolecular_interactions>
<chemistry_theories>Dispersion forces, polarizability, solvation energy.</chemistry_theories>
<overall_effect>High molar refractivity negatively affects solubilization as strong dispersion forces among additive molecules can diminish the solubility of the active material in highly polar solvents like water.</overall_effect>
</analysis>

#### Chemical Descriptor: Topological Polar Surface Area

<analysis>
<parameter_name>Topological Polar Surface Area (TPSA)</parameter_name>
<definition>Sum of the surface areas of all polar atoms in a molecule, typically oxygen and nitrogen, including attached hydrogens.</definition>
<physical_meaning>Indicates the molecule's ability to form hydrogen bonds and affects permeability and solubility.</physical_meaning>
<influence>Negative correlation (ranges from -0.048 to -0.493).</influence>
<intermolecular_interactions>Higher TPSA correlates with increased hydrogen-bonding potential but may reduce efficient solubilization by promote over-strong interactions with water, competing against the active material's solvation.</intermolecular_interactions>
<chemistry_theories>Hydrogen bonding, solvation dynamics, hydrophilic-lipophilic balance.</chemistry_theories>
<overall_effect>Higher TPSA generally reduces solubilization due to excessive hydrogen-bonding with water competing against active material interactions.</overall_effect>
</analysis>

#### Chemical Descriptor: Labute�s Approximate Surface Area

<analysis>
<parameter_name>Labute�s Approximate Surface Area (ASA)</parameter_name>
<definition>Calculated molecular surface area that approximates the accessible surface area for solvent interactions.</definition>
<physical_meaning>Higher ASA indicates a larger surface area for potential solvation interactions.</physical_meaning>
<influence>Negative correlation (ranges from -0.095 to -0.611).</influence>
<intermolecular_interactions>Greater surface area usually implies stronger overall solvation shells, but excessively large surface areas in additives may dilute the active material�s impact with solvent, reducing solubilization.</intermolecular_interactions>
<chemistry_theories>Surface chemistry, solvation theory.</chemistry_theories>
<overall_effect>Increasing ASA tends to negatively impact solubilization of the active material, possibly due to overwhelming solvation effects from additives, which compete with the active material itself for solvent interactions.</overall_effect>
</analysis>

#### Chemical Descriptor: Balaban�s J Index

<analysis>
<parameter_name>Balaban�s J Index</parameter_name>
<definition>Topological index that quantifies molecular branching and connectivity.</definition>
<physical_meaning>Represents the structural complexity of a molecule, with potential implications for molecular interactions and solubility properties.</physical_meaning>
<influence>Negative correlation (ranges from -0.068 to -0.463).</influence>
<intermolecular_interactions>More complex branch structures may hinder optimal spatial arrangements needed for effective solvation and increase steric hindrance potentially reducing solubility.</intermolecular_interactions>
<chemistry_theories>Steric effects, molecular topology.</chemistry_theories>
<overall_effect>Higher Balaban�s J Index indicates structural complexity that reduces solubilization efficiency due to potential steric hindrance and suboptimal packing arrangements with water molecules.</overall_effect>
</analysis>

#### Chemical Descriptor: Bertz CT Index

<analysis>
<parameter_name>Bertz CT Index</parameter_name>
<definition>Complexity index based on counts of molecular fragments and paths that reflect molecular entropy.</definition>
<physical_meaning>High Bertz CT Index indicates high molecular complexity, which can impact solubility characteristics.</physical_meaning>
<influence>Negative correlation (ranges from -0.042 to -0.572).</influence>
<intermolecular_interactions>Highly complex molecules with high entropy create more structural constraints, possibly reducing effective solubility by diminishing the ability to interact uniformly with the solvent.</intermolecular_interactions>
<chemistry_theories>Molecular entropy, solubility theory.</chemistry_theories>
<overall_effect>Higher Bertz CT Index correlates with decreased solubilization as complex molecular topologies may reduce effective interactions with the solvent needed for optimal solubilization of the active material.</overall_effect>
</analysis>

#### Chemical Descriptor: Melting Point

<analysis>
<parameter_name>Melting Point</parameter_name>
<definition>Temperature at which the additive transitions from a solid to a liquid phase.</definition>
<physical_meaning>Reflects the thermal stability and intermolecular forces of the additive. Higher melting points suggest stronger intermolecular forces within the additive.</physical_meaning>
<influence>Negative correlation (ranges from -0.030 to -0.428).</influence>
<intermolecular_interactions>Higher melting points indicate strong intermolecular forces, which can result in reduced solubilization efficiency in water by hindering interactions of the additive with water molecules.</intermolecular_interactions>
<chemistry_theories>Thermodynamics, intermolecular forces.</chemistry_theories>
<overall_effect>Higher melting points decrease solubilization due to strong intermolecular forces in additives which may oppose the solubilizing interactions necessary in an aqueous environment.</overall_effect>
</analysis>

---

Based on the provided data analysis, the different chemical descriptors influence the solubilization of active materials in various shapes aligned with their molecular interactions and theoretical principles.