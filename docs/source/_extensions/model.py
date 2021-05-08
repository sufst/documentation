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
        <script type="module">
          console.log("Model extension running");
          
          import * as THREE from 'https://cdn.skypack.dev/three@0.128.0';
          import { OrbitControls } from 'https://cdn.skypack.dev/three@0.128.0/examples/jsm/controls/OrbitControls.js';
          import { GLTFLoader } from 'https://cdn.skypack.dev/three@0.128.0/examples/jsm/loaders/GLTFLoader.js';
        
          // Get current script tag so we can insert around it
          const scriptElement = document.scripts[document.scripts.length - 1];
          const container = scriptElement.parentElement;
          
          // Calculate model canvas dimensions
          const canvasWidth = container.clientWidth;
          
          // Calculate height so canvas is 16:10 ratio
          const canvasHeight = canvasWidth / 16 * 10;
          
          const scene = new THREE.Scene();
          const camera = new THREE.PerspectiveCamera(75, canvasWidth / canvasHeight, 0.1, 1000);

          const renderer = new THREE.WebGLRenderer({antialias: true});
          renderer.setSize(canvasWidth, canvasHeight);
          renderer.gammaOutput = true;
          renderer.gammaFactor = 2.2;
          renderer.setPixelRatio(window.devicePixelRatio);
          
          // Add orbit controls
          const controls = new OrbitControls(camera, renderer.domElement);
          
          // Add ambient light for testing
          const amb_light = new THREE.AmbientLight(0xdef2ff, 1); // Blue-ish light
          scene.add(amb_light);
          
          // Add point light for testing
          const point_light = new THREE.PointLight( 0xff0000, 5, 100 );
          point_light.position.set(10, 10, 10);
          scene.add(point_light);
          
          // Add grid to visualise floor
          const size = 10;
          const divisions = 10;

          const grid = new THREE.GridHelper( size, divisions );
          scene.add(grid);
          
          //const geometry = new THREE.BoxGeometry();
          //const material = new THREE.MeshBasicMaterial({color: 0x00ff00});
          //const cube = new THREE.Mesh(geometry, material);
          //scene.add(cube);
          
          const loader = new GLTFLoader();

          loader.load('_static/%(name)s.glb', function(gltf) {
            scene.add(gltf.scene);
          }, undefined, function (error) {
            console.error(error);
          });
          
          // Update camera position
          camera.position.y = 0.4;
          camera.position.z = 0.4;
          controls.update();
          
          // Insert canvas at current script position in DOM
          scriptElement.parentElement.insertBefore(renderer.domElement, scriptElement);
          
          function animate() {
            requestAnimationFrame( animate );
            renderer.render( scene, camera );
          }
          animate();
        </script>
    """
    
    # Perform string subsitutions in markup template
    self.body.append(markup%{'name': node['name']})
    raise nodes.SkipNode


def setup(app):
    app.add_node(model,
                 html=(model_html, None))

    app.add_directive('model', Model)
    
    
