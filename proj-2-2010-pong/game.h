/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef GAME_H
#define GAME_H

#include "actor.h"

#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Actor;

class Game
{
public:
    Game(int height, int width);
    ~Game();
    void addActor(Actor* actor);
    void moveAll();
    Actor* get(int y, int x);
    Actor* getActor(int i);
    int getHeight();
    int getWidth();
    bool isWon();
    bool isLost();
    bool isInside(int y, int x);
    void write(ostream& out);
    int getUserCommand(int player = 0);
    void setUserCommand(int command, int player = 0);
    int getPoints(int player = 0);
    void scorePoints(int points, int player = 0);

    static const char BLANK = '.';

private:
    int height;
    int width;
    vector<Actor*> actors;
    map<int, int> commands;
    map<int, int> points;

    // In fact, a matrix is not required
    // ... but it would improve performance
    // Actor* map[MAX_HEIGHT][MAX_WIDTH];
};

#endif // GAME_H