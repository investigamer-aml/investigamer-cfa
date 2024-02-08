// src/components/LevelMap/LevelMap.js

import React from 'react';
import Level from '../Level/Level';
import levelsData from '../../utils/levelsData';
import './levelMap.css';

const LevelMap = () => {
    const renderLevels = () => levelsData.map(level => (
        <Level
            key={level.levelNumber}
            levelNumber={level.levelNumber}
            status={level.status}
            onClick={() => console.log(`Level ${level.levelNumber} clicked`)}
        />
    ));

    return (
        <div className="level-map">
            {renderLevels()}
        </div>
    );
};

export default LevelMap;

