// src/components/Level/Level.js

import React from 'react';
import './level.css';

const Level = ({ levelNumber, status, onClick }) => {
    const handleClick = () => {
        if (onClick && status === 'unlocked') {
            onClick(levelNumber);
        }
    };

    return (
        <div className={`level ${status}`} onClick={handleClick}>
            <span className="level-number">{levelNumber}</span>
        </div>
    );
};

export default Level;

