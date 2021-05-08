"""
Custom Sphinx extension to insert a viewable 3D model using WebGL.

To enable the extension, the '_extensions' path must be added in conf.py and
the 'model' extension should be added to the 'extensions' list.
  - For SUFST, this is already done

USAGE:

 .. model::
    :name: Test
    
Where,
':name:' defines the filename relative from the file you insert the directive.

For example, if you are in the RST file './sub-folder/index.rst' and you add
the following directive:
 .. model::
    :name: model/pcb.vrml
    
A 3D model called 'pcb.vrml' found in './sub-folder/model' would be added to
the documentation.
"""

from docutils import nodes
from docutils.nodes import Body, Element
from docutils.parsers.rst import Directive, directives

class model(Body, Element):
   pass


class Model(Directive):
    required_arguments = 0
    has_content = False
    option_spec = {'name': directives.unchanged}

    def run(self):
        # Create html node in markup
        node = model()
        node['name'] = self.options['name']
        return [node]

def model_html(self, node):
    # Define HTML markup to insert

    markup = """
        <script src="_static/three.js"></script>

        <script>
          console.log("Model extension running");
        
          // Get current script tag so we can insert around it
          scriptElement = document.scripts[document.scripts.length - 1];
          container = scriptElement.parentElement;
          
          // Calculate model canvas dimensions
          canvasWidth = container.clientWidth;
          
          // Calculate height so canvas is 16:10 ratio
          canvasHeight = canvasWidth / 16 * 10;
          
          const scene = new THREE.Scene();
          const camera = new THREE.PerspectiveCamera(75, canvasWidth / canvasHeight, 0.1, 1000);

          const renderer = new THREE.WebGLRenderer();
          renderer.setSize(canvasWidth, canvasHeight);
          
          
          const geometry = new THREE.BoxGeometry();
          const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
          const cube = new THREE.Mesh( geometry, material );
          scene.add( cube );

          camera.position.z = 5;
          
          var animate = function () {
            requestAnimationFrame( animate );

            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;

            renderer.render( scene, camera );
          };

          animate();


          // Insert canvas at current script position in DOM
          scriptElement.parentElement.insertBefore(renderer.domElement, scriptElement);
        </script>
    """
    
    # Perform string subsitutions in markup template
    self.body.append(markup%{'name': node['name']})
    raise nodes.SkipNode


def setup(app):
    app.add_node(model,
                 html=(model_html, None))

    app.add_directive('model', Model)
    
    
