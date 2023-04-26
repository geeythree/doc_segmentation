import matplotlib.pyplot as plt

def show_box(box: dict, ax):
    ''' 
    Draws the segmentation bbox 
    '''
    x0, y0, w, h = box[0], box[1], box[2], box[3]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2)) 

def show_mask(categories: dict, annotation: dict, ax):
    ''' 
    Draws the segmentation mask 
    '''

    colors = {'title': 'red',
          'text': 'lime',
          'figure': 'blue',    
          'table': 'yellow',
          'list': 'aqua'}
    #print(annotation)
    fill = (colors[categories[annotation['category_id'] - 1]['name']]) 
    #print(fill)
    polygon = annotation['segmentation'][0]
    reshape_poly = [tuple(polygon[i:i+2]) for i in range(0, len(polygon), 2)]


    ax.add_patch(plt.Polygon(reshape_poly, color=fill, alpha = 0.3))

