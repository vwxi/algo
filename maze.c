/*
 * maze.c - some maze stuff
 */

#include <stdio.h>
#include <stdlib.h>

#define MAZE_W 22
#define MAZE_H 21
#define MAZE_SZ (MAZE_W * MAZE_H)

#define TRUE 1
#define FALSE 0

#define WALL '#'

#define IDX(x, y) (MAZE_W * x + y)

struct stack {
	int 	s_capacity;
	int 	s_idx;
	int*	s_items;	
};

struct maze {
	struct stack* m_path;
	char 	m_maze[MAZE_W][MAZE_H];
	char 	m_seen[MAZE_SZ];
	int 	m_endx;
	int 	m_endy;
	int 	m_solved;
};

struct stack* stack_new()
{
	struct stack* s = (struct stack*)malloc(sizeof(struct stack));
	if(!s)
		return NULL;

	s->s_capacity = MAZE_SZ;
	s->s_idx = -1;
	s->s_items = (int*)malloc(sizeof(int)*s->s_capacity);
	
	if(!s->s_items) {
		free(s);
		return NULL;
	}

	return s;
}

void stack_destroy(struct stack* s)
{
	if(s) {
		if(s->s_items)
			free(s->s_items);

		free(s);
		s->s_items = NULL;
		s = NULL;
	}
}

int stack_full(struct stack* s)
{
	return s->s_idx == s->s_capacity - 1;
}

int stack_empty(struct stack* s)
{
	return !s->s_idx;
}

int stack_push(struct stack* s, int v)
{
	if(!s || 
		!s->s_items || 
		stack_full(s)) return FALSE;

	s->s_items[++s->s_idx] = v;
	return TRUE;
}

int stack_pop(struct stack* s)
{
	if(!s ||
		!s->s_items ||
		stack_empty(s)) return FALSE;

	/* we do not need the popped result */
	s->s_idx--;
	return TRUE;
}

int stack_peek(struct stack* s)
{
	if(!s ||
		!s->s_items ||
		stack_empty(s)) return FALSE;

	return s->s_items[s->s_idx];	
}

/* a recursive solution */
int maze_solve_r(
	struct maze* m,
	int x,
	int y
)
{
	if(m->m_solved || /* have we solved it */
		m->m_maze[x][y] == WALL || /* is this a wall */
		m->m_seen[IDX(x, y)]) /* have we seen this tile before */
		return FALSE;

	if(x == m->m_endx &&
		y == m->m_endy) { /* is this the end */
		m->m_solved = TRUE;
		return FALSE;		
	}	

	if(y != 0 || y != MAZE_H - 1 || 
		x != 0 || x != MAZE_W - 1) { /* are we within the boundaries */
			return FALSE;
	}

	/* we have seen this tile before */
	m->m_seen[IDX(x, y)] = TRUE;

	/* we now consider this a possible path */
	stack_push(m->m_path, IDX(x, y));

	if(maze_solve_r(m, x, y-1) ||
		maze_solve_r(m, x, y+1) ||
		maze_solve_r(m, x-1, y) ||
		maze_solve_r(m, x+1, y)) {
		/* this is a good tile */
		return TRUE;		
	}

	/* this is not a good tile */
	stack_pop(m->m_path);	
	return FALSE;
}

int main()
{
	struct maze m;
	m.m_path = stack_new();

	/* TODO: setup maze */
	/*
	printf("%s\n", (maze_solve_r(&m, 1, 1)) ? "success" : "failure");
		*/
	stack_destroy(m.m_path);
	return 0;
}
