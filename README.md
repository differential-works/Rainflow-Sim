# Rainflow-Sim
A simplified rain flow simulation template using Rhino 3D and Grasshopper to assist in early-stage architectural or landscape design. 

![image](https://github.com/differential-works/Rainflow-Sim/blob/main/241030_Rain%20Sim_GitHub.gif) 

In an era of increasing climate uncertainty and rising urbanization, understanding water flow patterns has become crucial for resilient design. Urban flooding, landscape erosion, and inadequate drainage systems pose significant risks to both infrastructure and communities. Moreover, proper roof drainage design is essential for building longevity and occupant safety. Early-stage water flow analysis can help identify potential problems before they manifest, leading to more informed design decisions and more resilient built environments.

This Grasshopper script provides architects, urban planners, and designers an accessible tool for analyzing potential water flow patterns on terrain surfaces and roof geometries. By visualizing and understanding approximate water flow behaviour in landscape, urban, and architectural contexts, designers can make more informed decisions about site planning, drainage strategies, and risk mitigation.

## Overview
This tool uses a simplified physics model to simulate water flow on mesh surfaces, providing indicative visualization of:

- Potential water flow paths
- Areas of water accumulation through flow line clustering
- Possible drainage patterns
- Potential flood risk zones in urban areas
- Roof drainage patterns and critical points
- Indicative locations for gutters and overflow zones

## Features
### Water Flow Simulation
The script simulates water particles flowing over a mesh surface using a combination of gravitational force and momentum. Each particle:
- Follows the terrain/roof geometry
- Maintains directional momentum
- Responds to gravitational pull
- Creates a continuous flow path

### Flow Line Clustering
- The tool includes functionality to:
- Group flow lines that are within a specified distance threshold
- Identify areas where multiple flow paths converge
- Highlight potential high-risk zones for water accumulation
- Visualize primary drainage patterns
- Indicate optimal locations for gutters and overflow points on roofs
- Help determine appropriate gutter sizes based on flow concentration

### Parameters
- ```step```: Controls the granularity of the analysis
- ```iterations```: Determines how far the water flows
- ```momentum```: Balances between terrain-following and gravitational behavior (0-1)
  - ```0```: Pure gravitational flow
  - ```1```: Strong terrain-following behavior
  - Recommended range for water simulation: ```0.6-0.8```
- ```cluster_threshold```: Distance threshold for grouping nearby flow lines

## Implementation
The tool consists of two main parts:
1. Water flow simulation implemented in GHPython, leveraging:
  - RhinoCommon for geometry operations
  - GHPython for Grasshopper integration
  - Native Python functionality for calculations
2. Flow line clustering and analysis implemented through standard Grasshopper components for:
  - Proximity analysis
  - Group formation
  - Pattern identification
  - Risk zone visualization

This dual implementation approach makes the tool both powerful and easily customizable within the familiar Grasshopper environment.

## Limitations and Disclaimer
This tool is intended for preliminary analysis and visualization purposes only. It should not be used as the sole basis for critical design decisions or engineering calculations. The simulation does NOT account for:
- Water volume and mass
- Ground material permeability or absorption
- Existing drainage infrastructure capacity
- Surface friction or material properties
- Water accumulation or pooling
- Flow splitting or merging
- Variable velocity based on slope
- Real fluid dynamics (turbulence, pressure, etc.)
- Rainfall intensity or duration
- Subsurface water movement
- Existing flood prevention measures
- Local drainage regulations and requirements
- Specific roof material characteristics
- Building code requirements for drainage systems

## Intended Use
This tool is best used for:
- Early-stage site analysis
- Preliminary drainage strategy development
- Urban risk assessment visualization
- Roof drainage design exploration
- Educational purposes
- Communication with stakeholders
- Identifying areas requiring detailed hydrological study
- Initial gutter placement and sizing studies

## Requirements
- Rhinoceros 3D (version 8)
- Grasshopper
- GHPython

## License
This project is licensed under the MIT License - see the LICENSE file for details. This means you can freely use, modify, and distribute this tool, but please provide attribution to the original authors.

## Contributing
We welcome contributions to improve the script! If you encounter any issues or have suggestions for enhancements, please feel free to contact us at hello@differential.works.
