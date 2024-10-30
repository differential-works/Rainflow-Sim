import Rhino.Geometry as rg
import scriptcontext as sc
import math

def get_direction_vector(p1, p2, step_size):
    """Calculate normalized direction vector between two points"""
    vec = rg.Vector3d(p2 - p1)
    if vec.Length > 0:
        vec.Unitize()
        return vec * step_size
    return rg.Vector3d(0,0,0)

# Create flow lines
flow_lines = []
for i in range(0, len(points), 3):
    x = points[i]
    y = points[i+1]
    z = points[i+2]
    start_pt = rg.Point3d(x, y, z)
    flow_points = [start_pt]
    
    # Create flow line
    for j in range(iterations):
        last_point = flow_points[-1]
        
        # Calculate movement vector
        if len(flow_points) > 1:
            # Get direction from last segment (momentum)
            prev_vector = get_direction_vector(flow_points[-2], last_point, step)
            # Combine with downward vector (weighted sum)
            down_vector = rg.Vector3d(0, 0, -step)
            
            # Apply weights: momentum_weight for previous direction, (1-momentum_weight) for gravity
            movement_vector = prev_vector * momentum + down_vector * (1.0 - momentum)
            
            # Normalize and scale to step size
            if movement_vector.Length > 0:
                movement_vector.Unitize()
                movement_vector *= step
        else:
            # For first iteration, just move down
            movement_vector = rg.Vector3d(0, 0, -step)
        
        # Create next point
        next_point = rg.Point3d(last_point) + movement_vector
        
        # Project to mesh
        projected = mesh.ClosestPoint(next_point)
        if projected:
            flow_points.append(rg.Point3d(projected))
    
    if len(flow_points) > 1:
        flow_lines.append(rg.Polyline(flow_points))

# Single output
a = flow_lines