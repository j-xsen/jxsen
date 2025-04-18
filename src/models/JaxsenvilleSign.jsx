/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
Command: npx gltfjsx@6.5.3 jaxsenvillesign.glb --transform 
Files: jaxsenvillesign.glb [495.69KB] > Z:\art\models\jaxsenvillesign\jaxsenvillesign-transformed.glb [35.21KB] (93%)
*/

import React from 'react'
import { useGLTF } from '@react-three/drei'
import { useFrame } from '@react-three/fiber'

export function JaxsenvilleSign(props) {
  const { nodes, materials } = useGLTF('/models/jaxsenvillesign-transformed.glb')
  const mesh = React.useRef()
  const [rotatingLeft, setRotatingLeft] = React.useState(true)
  const [hovered, setHovered] = React.useState(false)
  const speed = 0.0055
  const maxRotation = 0.4
  const defaultScale = 0.65
  const hoveredScale = 0.7
    
  useFrame(() => {
    if (rotatingLeft) {
        mesh.current.rotation.y -= speed
        if ( mesh.current.rotation.y <= -maxRotation) {
            setRotatingLeft(false)
        }
    } else {
        mesh.current.rotation.y += speed
        if ( mesh.current.rotation.y >= maxRotation) {
            setRotatingLeft(true)
        }
    }
    mesh.current.rotation.y 
  })

  return (
    <group {...props} dispose={null} ref={mesh} scale={hovered ? hoveredScale : defaultScale}
    onPointerOver={(event) => setHovered(true)}
    onPointerOut={(event) => setHovered(false)}
    onClick={()=>window.open("https://jaxsenville.com/", "_blank")}>
      <mesh geometry={nodes.roof.geometry} material={materials.PaletteMaterial003} />
      <mesh geometry={nodes.Cube.geometry} material={materials.PaletteMaterial001} />
      <mesh geometry={nodes.Cube_1.geometry} material={materials.PaletteMaterial002} />
      <mesh geometry={nodes.Cube001.geometry} material={materials.PaletteMaterial001} />
      <mesh geometry={nodes.Cube001_1.geometry} material={materials.PaletteMaterial002} />
      <mesh geometry={nodes.Cube004.geometry} material={materials.PaletteMaterial004} />
      <mesh geometry={nodes.Cube004_1.geometry} material={materials.PaletteMaterial005} />
    </group>
  )
}

useGLTF.preload('/models/jaxsenvillesign-transformed.glb')
