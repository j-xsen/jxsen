import { extend } from "@react-three/fiber"
import React from "react"
import LetterMesh from "./LetterMesh";
import { Box3, Object3D, Vector3 } from "three";

export default function WordMesh(props) {
    const centerAlign = (wordGroup) => {
        const boundingBox = new Box3().setFromObject(wordGroup)
        const size = new Vector3()
        boundingBox.getSize(size)
        wordGroup.position.x = - (size.x / 2)
        return wordGroup;
    };

    const populateWord = () => {
        let splitIndex = 0;

        const letters = props.word.split("").map((letter, index) => {
            if (letter === " " || letter === ",") {
                if (letter === " ") {
                    splitIndex = index + 1;
                }
                return null;
            }

            return (
                <LetterMesh
                    key={index}
                    letter={letter}
                    font={props.font}
                    charPos={index - splitIndex}
                    line={splitIndex ? 1 : 0}
                    color="white"
                />
            )
        })

        return <group name="WordGroup" ref={groupRef}>{letters}</group>
    }

    const groupRef = React.useRef(); // Create a ref for the group

    React.useEffect(() => {
        if (groupRef.current) {
            centerAlign(groupRef.current); // Pass the group to centerAlign
        }
    }, [groupRef]);

    return populateWord();
}
